import unittest
from flask import current_app
from app import create_app, db
from app.models.text_history import TextHistory
from app.models.text import Text


class TextHistoryTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_text_history_save(self):
        text = Text()
        text.content = "Hola mundo"
        text.length = len(text.content)
        text.language = "es"
        text.save()

        # Guarda una versión del texto
        history = TextHistory()
        history.text_id = text.id
        history.content = "Hola mundo"
        history.save()

        self.assertGreaterEqual(history.id, 1)
        self.assertEqual(history.text_id, text.id)
        self.assertEqual(history.content, "Hola mundo")

    def test_change_to_version(self):
        # Crea un texto y guarda dos versiones
        text = Text()
        text.content = "Hello world"
        text.length = len(text.content)
        text.language = "en"
        text.save()

        version1 = TextHistory()
        version1.text_id = text.id
        version1.content = "Hola mundo"
        version1.save()

        version2 = TextHistory()
        version2.text_id = text.id
        version2.content = "Bonjour monde"
        version2.save()

        # Cambia a la primera versión y verifica que el contenido cambie
        version1.change_to_version(version1.id)
        updated_text = Text.find(text.id)
        self.assertEqual(updated_text.content, version1.content)

        # Cambia a la segunda versión y verifica que el contenido cambie
        version2.change_to_version(version2.id)
        updated_text = Text.find(text.id)
        self.assertEqual(updated_text.content, version2.content)


if __name__ == "__main__":
    unittest.main()
