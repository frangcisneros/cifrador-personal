# ------------------------------- importaciones ------------------------------ #
import unittest
import requests
from app.models import Text
from app import create_app, db
from app.services import EncryptService
from app.repositories import TextRepository

# ----------------------------- fin importaciones ---------------------------- #

# ------------------------- servicios y repositorios ------------------------- #
encrypt_service = EncryptService()
text_repository = TextRepository()
# ----------------------- fin servicios y repositorios ----------------------- #


class TestRequests(unittest.TestCase):
    def setUp(self):
        # --------------------------- seteo atributos texto -------------------------- #
        self.CONTENT_PRUEBA = "Hola mundo"
        self.LENGTH_PRUEBA = len(self.CONTENT_PRUEBA)
        self.LANGUAGE_PRUEBA = "es"
        # ------------------------- fin seteo atributos texto ------------------------ #
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    # * METODO PARA DESTRUIR LA BASE DE DATOS
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    # * GETTER DE TEXTO
    def __get_text(self):
        text = Text()
        text.content = self.CONTENT_PRUEBA
        text.length = self.LENGTH_PRUEBA
        text.language = self.LANGUAGE_PRUEBA
        return text

    def test_display_all_texts(self):
        text = self.__get_text()
        text_repository.save(text)
        response = requests.get("http://127.0.0.1:5000/all_texts")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")

    def test_search_texts(self):
        text = self.__get_text()
        text_repository.save(text)
        response = requests.get("http://127.0.0.1:5000/get_text/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")

    def test_add_text(self):
        response = requests.post(
            "http://127.0.0.1:5000/add_text",
            json={"content": "Hola mundo add", "language": "es"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response.json(), {"message": "Text added successfully"})


if __name__ == "__main__":
    unittest.main()
