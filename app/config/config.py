from asyncio.log import logger
from dotenv import load_dotenv
from pathlib import Path
import os

basedir = os.path.abspath(Path(__file__).parents[2])

load_dotenv(os.path.join(basedir, ".env"))


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    @staticmethod
    def init_app(app):
        pass


class TestConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URI")


class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URI")


class ProductionConfig(Config):
    """
    Configuración de producción para la aplicación.
    Atributos:
    - DEBUG: Valor booleano que indica si el modo de depuración está activado o desactivado.
    - TESTING: Valor booleano que indica si las pruebas están habilitadas o deshabilitadas.
    - SQLALCHEMY_RECORD_QUERIES: Valor booleano que indica si se deben registrar las consultas de SQLAlchemy.
    - SQLALCHEMY_DATABASE_URI: Cadena que representa la URI de la base de datos de producción.
    Métodos:
    - init_app: Método de clase que inicializa la aplicación con la configuración de producción.
    """

    DEBUG = False
    TESTING = False
    SQLALCHEMY_RECORD_QUERIES = False

    SQLALCHEMY_DATABASE_URI = os.environ.get("PROD_DATABASE_URI")

    @classmethod
    def init_app(cls, app):
        """
        Inicializa la aplicación con la configuración de producción.
        Parámetros:
        - app: Instancia de la aplicación Flask.
        Retorna:
        None
        """
        Config.init_app(app)


def factory(app):
    """
    Devuelve la configuración correspondiente según la aplicación especificada.
    Parámetros:
    - app: Una cadena que representa la aplicación para la cual se desea obtener la configuración.
    Retorna:
    - La configuración correspondiente a la aplicación especificada.
    """
    configuration = {
        "testing": TestConfig,
        "development": DevelopmentConfig,
        "production": ProductionConfig,
    }

    return configuration[app]
