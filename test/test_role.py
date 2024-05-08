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

    def tearDown(self):
        # Desactiva y limpia el contexto de la aplicación
        self.app_context.pop()

    # Prueba si la aplicación Flask se crea correctamente
    def test_app(self):
        self.assertIsNotNone(current_app)
    
    # Prueba la creación de roles
    def test_role(self):
        # Crea una instancia de la clase Role
        user = Role()
        # Establece el nombre y la descripción del rol
        user.name = 'ROLE_ADMIN'
        user.description = 'Administrator'
        # Verifica que el nombre y la descripción del rol sean correctos
        self.assertTrue(user.name, 'ROLE_ADMIN')
        self.assertTrue(user.description, 'Administrator')

if __name__ == '__main__':
    # Ejecuta el conjunto de pruebas si el script se ejecuta directamente
    unittest.main()
