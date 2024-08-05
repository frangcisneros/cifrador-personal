import unittest
from flask import current_app
from app import create_app, db
from app.models import Text, TextHistory
from cryptography.fernet import Fernet
from app.services import UserService, EncryptService
from app.repositories import TextRepository


encrypt_service = EncryptService()
text_repository = TextRepository()


class TextTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)

    def set_text_attributes(self, text):
        text.content = "Hola mundo"
        text.length = len(text.content)
        text.language = "es"

    def assert_text_content(self, text):
        self.assertEqual(text.content, "Hola mundo")
        self.assertEqual(text.length, 10)
        self.assertEqual(text.language, "es")

    def test_text(self):
        text = Text()
        self.set_text_attributes(text)
        self.assert_text_content(text)

    def test_text_save(self):
        text = Text()
        self.set_text_attributes(text)
        text_repository.save(text)

        self.assertGreaterEqual(text.id, 1)
        self.assert_text_content(text)

    def test_text_delete(self):
        text = Text()
        self.set_text_attributes(text)
        text_repository.save(text)
        text_repository.delete(text)

        self.assertIsNone(Text.query.get(text.id))

    def test_text_find(self):
        text = Text()
        self.set_text_attributes(text)
        text_repository.save(text)
        text_find = text_repository.find(1)
        self.assertIsNotNone(text_find)
        self.assertEqual(text_find.id, text.id)
        self.assertEqual(text_find.content, text.content)

    def test_encrypt_content(self):
        text = Text()
        self.set_text_attributes(text)
        text_repository.save(text)

        key = Fernet.generate_key()

        encrypt_service.encrypt_content(text, key)

        self.assertNotEqual(text.content, "Hola mundo")
        self.assertIsInstance(text.content, str)

    # metodo para desencritar
    def test_decrypt_content(self):
        text = Text()
        self.set_text_attributes(text)
        text_repository.save(text)

        key = Fernet.generate_key()
        encrypt_service.encrypt_content(text, key)

        encrypt_service.decrypt_content(text, key)

        self.assertEqual(text.content, "Hola mundo")

    def test_change_content(self):
        # Crea un objeto Text y guarda una versión
        text = Text()
        self.set_text_attributes(text)
        text_repository.save(text)

        old_content = text.content

        # Cambia el contenido
        new_content = "Hola mundo"
        encrypt_service.change_content(text, new_content)

        # Verifica que el contenido haya cambiado
        self.assertEqual(text.content, new_content)

        # Verifica que se haya guardado la versión anterior en TextHistory
        history = TextHistory.query.filter_by(text_id=text.id).first()
        self.assertIsNotNone(history)
        self.assertEqual(history.content, old_content)

    # test para comprobar que funciona la relacion entres usuarios y textos
    def test_user_text(self):
        from app.models.user import User
        from app.models.user_data import UserData

        # Crea un objeto UserData con información de prueba
        data = UserData()
        data.firstname = "Pablo"
        data.lastname = "Prats"
        data.address = "Address 1234"
        data.city = "San Rafael"
        data.country = "Argentina"
        data.phone = "54260123456789"

        # Crea un objeto User y establece sus atributos
        user = User(data)
        user.email = "test@test.com"
        user.username = "pabloprats"
        user.password = "Qvv3r7y"
        user_service = UserService()
        user_service.save(user)

        # Crea un objeto Text y establece sus atributos
        text = Text()
        self.set_text_attributes(text)
        text.user_id = user.id
        text_repository.save(text)


if __name__ == "__main__":
    unittest.main()
