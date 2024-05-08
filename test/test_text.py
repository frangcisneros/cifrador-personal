import unittest
from flask import current_app
from app import create_app, db
from app.models.text import Text


class TextTestCase(unittest.TestCase):
    def setUp(self):
        # Crea una instancia de la aplicacion Flask para pruebas
        self.app = create_app()
        # Crea un contexto de la aplicacion y lo activa
        self.app_context = self.app.app_context()
        self.app_context.push()
        # Crea todas las tablas en la base de datos para las pruebas
        db.create_all()

    def tearDown(self):
        # Elimina todas las tablas y el contexto de la aplicacion
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app(self):
        # Prueba que la aplicacion existe
        self.assertIsNotNone(current_app)

    # prueba la creacion de un texto
    def test_text(self):
        # crea un objeto Text
        text = Text()
        text.content = "Hola mundo"
        text.length = len(text.content)
        text.language = "es"
        # verificamos que los atributos del texto sean correctos
        self.assertEqual(text.content, "Hola mundo")
        self.assertEqual(text.length, 10)
        self.assertEqual(text.language, "es")

    def test_text_save(self):
        # crea un objeto Text
        text = Text()
        text.content = "Hola mundo"
        text.length = len(text.content)
        text.language = "es"
        # guarda el texto en la base de datos
        text.save()

        self.assertGreaterEqual(text.id, 1)
        self.assertEqual(text.content, "Hola mundo")
        self.assertEqual(text.length, 10)
        self.assertEqual(text.language, "es")

    def test_text_delete(self):
        # crea un objeto Text
        text = Text()
        text.content = "Hola mundo"
        text.length = len(text.content)
        text.language = "es"
        # guarda el texto en la base de datos
        text.save()
        # elimina el texto de la base de datos
        text.delete()
        # verifica que el texto no exista en la base de datos
        self.assertIsNone(Text.query.get(text.id))

    def test_text_find(self):
        # crea un objeto Text
        text = Text()
        text.content = "Hola mundo"
        text.length = len(text.content)
        text.language = "es"
        # guarda el texto en la base de datos
        text.save()
        text_find = Text.find(1)
        self.assertIsNotNone(text_find)
        self.assertEqual(text_find.id, text.id)
        self.assertEqual(text_find.content, text.content)


if __name__ == "__main__":
    unittest.main()
