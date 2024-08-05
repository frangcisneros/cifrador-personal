import unittest
from flask import current_app
from app import create_app

class AppTestCase(unittest.TestCase):
    # Método de configuración que se ejecuta antes de cada prueba
    def setUp(self):
        # Crea una instancia de la aplicación Flask para pruebas
        self.app = create_app()
        # Crea un contexto de la aplicación y lo activa
        self.app_context = self.app.app_context()
        self.app_context.push()

    # Método de limpieza que se ejecuta después de cada prueba
    def tearDown(self):
        # Desactiva y limpia el contexto de la aplicación
        self.app_context.pop()

    # Método de prueba para verificar si la aplicación Flask se crea correctamente
    def test_app(self):
        # Verifica que el objeto current_app no sea None
        self.assertIsNotNone(current_app)

# Ejecuta el conjunto de pruebas si el script se ejecuta directamente
if __name__ == '__main__':
    unittest.main()
