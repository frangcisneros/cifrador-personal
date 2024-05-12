import unittest
from flask import current_app
from app import create_app
from app.models import Role


class RoleTestCase(unittest.TestCase):
    def setUp(self):
        # Crea una instancia de la aplicación Flask para pruebas
        self.app = create_app()
        # Crea un contexto de la aplicación y lo activa
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.ROL_NAME = "ROLE_ADMIN"
        self.ROL_DESCRIPCION = "Administrator"

    def tearDown(self):
        # Desactiva y limpia el contexto de la aplicación
        self.app_context.pop()

    # Prueba si la aplicación Flask se crea correctamente
    def test_app(self):
        self.assertIsNotNone(current_app)

    # Prueba la creación de roles
    def test_role(self):
        role = self.__get_role()
        self.assertTrue(role.name, "ROLE_ADMIN")
        self.assertTrue(role.description, "Administrator")

    def __get_role(self) -> Role:
        role = Role()
        role.name = self.ROL_NAME
        role.description = self.ROL_DESCRIPCION
        return role


if __name__ == "__main__":
    # Ejecuta el conjunto de pruebas si el script se ejecuta directamente
    unittest.main()
