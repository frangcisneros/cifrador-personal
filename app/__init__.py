# Importaciones necesarias
from flask import Flask  # Importa la clase Flask para crear la aplicación
from flask_marshmallow import (
    Marshmallow,
)  # Importa la extensión Marshmallow para la serialización y deserialización de objetos
import os  # Importa el módulo os para interactuar con el sistema operativo
from flask_migrate import (
    Migrate,
)  # Importa la extensión Flask-Migrate para migraciones de base de datos
from flask_sqlalchemy import (
    SQLAlchemy,
)  # Importa la extensión SQLAlchemy para interactuar con bases de datos relacionales
from app.config import (
    config,
)  # Importa la configuración de la aplicación desde el paquete app.config

# Crea instancias de las extensiones
db = SQLAlchemy()  # Instancia de SQLAlchemy para interactuar con la base de datos
migrate = Migrate()  # Instancia de Flask-Migrate para migraciones de base de datos
ma = (
    Marshmallow()
)  # Instancia de Marshmallow para la serialización y deserialización de objetos


# Define una función para crear la aplicación Flask
def create_app() -> Flask:
    """
    Using an Application Factory
    Ref: Book Flask Web Development Page 78
    """
    # Obtiene el contexto de la aplicación desde la variable de entorno FLASK_CONTEXT
    app_context = os.getenv("FLASK_CONTEXT")

    # Crea una instancia de la aplicación Flask
    app = Flask(__name__)  # El nombre del módulo actual se pasa como argumento

    # Obtiene la configuración correspondiente al contexto de la aplicación (desarrollo, producción, etc.)
    config_instance = config.factory(app_context if app_context else "development")
    app.config.from_object(
        config_instance
    )  # Configura la aplicación con la instancia de configuración obtenida

    # Inicializa las extensiones con la aplicación
    ma.init_app(app)  # Inicializa Marshmallow con la aplicación
    db.init_app(app)  # Inicializa SQLAlchemy con la aplicación
    migrate.init_app(
        app, db
    )  # Inicializa Flask-Migrate con la aplicación y la instancia de SQLAlchemy

    # Registra los blueprints (enrutadores modulares) en la aplicación
    from app.resources import (
        home,
    )  # Importa el blueprint 'home' desde el paquete app.resources

    app.register_blueprint(
        home, url_prefix="/api/v1"
    )  # Registra el blueprint 'home' con un prefijo de URL '/api/v1'

    # Define un contexto de shell para interactuar con la aplicación en el shell interactivo
    @app.shell_context_processor
    def shell_context():
        return {
            "app": app
        }  # Devuelve un diccionario con la aplicación para el contexto de shell

    return app  # Retorna la aplicación Flask creada
