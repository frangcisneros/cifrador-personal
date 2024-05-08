import unittest
from sqlalchemy import text

from app import create_app, db

class ConnectionTestCase(unittest.TestCase):
    def setUp(self):
        # Crea una instancia de la aplicación Flask para pruebas
        self.app = create_app()
        # Crea un contexto de la aplicación y lo activa
        self.app_context = self.app.app_context()
        self.app_context.push()
        # Crea todas las tablas en la base de datos para las pruebas
        db.create_all()

    def tearDown(self):
        # Elimina la sesión de la base de datos y todas las tablas creadas
        db.session.remove()
        db.drop_all()
        # Desactiva y limpia el contexto de la aplicación
        self.app_context.pop()

    # Prueba la conexión a la base de datos
    def test_db_connection(self):
        # Ejecuta una consulta de prueba en la base de datos
        result = db.session.query(text("'Hello world'")).one()
        # Verifica que el resultado de la consulta sea 'Hello world'
        self.assertEqual(result[0], 'Hello world')

if __name__ == '__main__':
    # Ejecuta el conjunto de pruebas si el script se ejecuta directamente
    unittest.main()
