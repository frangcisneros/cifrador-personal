# Importaciones necesarias
from asyncio.log import (
    logger,
)  # Importa el registro asincrónico (no se utiliza en este código)
from dotenv import (
    load_dotenv,
)  # Importa la función para cargar variables de entorno desde un archivo .env
from pathlib import (
    Path,
)  # Importa la clase Path de la biblioteca pathlib para trabajar con rutas de archivos
import os  # Importa el módulo os para interactuar con el sistema operativo

# Obtiene la ruta absoluta del directorio base de la aplicación
basedir = os.path.abspath(Path(__file__).parents[2])

# Carga las variables de entorno desde un archivo .env en el directorio base de la aplicación
load_dotenv(os.path.join(basedir, ".env"))


# Clase base para la configuración de la aplicación
class Config(object):
    TESTING = False  # Modo de pruebas desactivado por defecto
    SQLALCHEMY_TRACK_MODIFICATIONS = (
        False  # Desactiva el seguimiento de modificaciones en SQLAlchemy
    )
    SQLALCHEMY_RECORD_QUERIES = True  # Activa el registro de consultas en SQLAlchemy

    # Método estático para inicializar la aplicación con esta configuración
    @staticmethod
    def init_app(app):
        pass  # No hace nada por defecto


# Clase de configuración para el entorno de desarrollo
class DevelopmentConfig(Config):
    TESTING = True  # Modo de pruebas activado
    DEBUG = True  # Modo de depuración activado
    SQLALCHEMY_TRACK_MODIFICATIONS = (
        True  # Activa el seguimiento de modificaciones en SQLAlchemy
    )
    # Obtiene la URI de la base de datos de las variables de entorno
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URI")


# Clase de configuración para el entorno de producción
class ProductionConfig(Config):
    DEBUG = False  # Modo de depuración desactivado
    TESTING = False  # Modo de pruebas desactivado
    SQLALCHEMY_RECORD_QUERIES = (
        False  # Desactiva el registro de consultas en SQLAlchemy
    )
    # Obtiene la URI de la base de datos de las variables de entorno
    SQLALCHEMY_DATABASE_URI = os.environ.get("PROD_DATABASE_URI")

    # Método de inicialización de la aplicación para el entorno de producción
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)  # Llama al método init_app de la clase base


# Función de fábrica que devuelve la clase de configuración según el entorno especificado
def factory(app):
    configuration = {
        "development": DevelopmentConfig,  # Clase de configuración para el entorno de desarrollo
        "production": ProductionConfig,  # Clase de configuración para el entorno de producción
    }

    return configuration[
        app
    ]  # Devuelve la clase de configuración correspondiente al entorno
