import unittest

from flask import current_app
from app import create_app
from dotenv import load_dotenv
from pathlib import Path
from app.mapping.response_schema import ResponseSchema
from app.services.response_message import ResponseBuilder
import os

basedir = os.path.abspath(Path(__file__).parents[2])

load_dotenv(os.path.join(basedir, ".env"))


class HomeResourceTestCase(unittest.TestCase):

    def setUp(self):
        os.environ["FLASK_CONTEXT"] = "testing"
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_index(self):
        message = (
            ResponseBuilder()
            .set_message("Bienvenidos")
            .set_status_code(200)
            .set_data({"title": "API Auth"})
            .build()
        )
        client = self.app.test_client(use_cookies=True)
        responseSchema = ResponseSchema()
        response = client.get(os.environ.get("URL_API"))
        self.assertEqual(response.status_code, 200)
        response = responseSchema.load(response.get_json())
        self.assertEqual(message.message, response["message"])
        self.assertEqual(message.status_code, response["status_code"])
        self.assertEqual(message.data, response["data"])


if __name__ == "__main__":
    unittest.main()
