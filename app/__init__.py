from flask import Flask
from flask_marshmallow import Marshmallow
import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.config import config


db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


def create_app() -> Flask:
    app_context = os.getenv("FLASK_CONTEXT")

    app = Flask(__name__)

    config_instance = config.factory(app_context if app_context else "development")
    app.config.from_object(config_instance)

    ma.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from app.resources import home, user

    app.register_blueprint(home, url_prefix="/api/v1")
    app.register_blueprint(user, url_prefix="/api/v1")

    @app.shell_context_processor
    def shell_context():
        return {"app": app}

    return app
