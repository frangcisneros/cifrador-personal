from app import create_app, db
from app.routes.index import index
from app.services import roles
import os

from error_handler.handlers import register_error_handlers
import logging

# Ref: https://docs.python.org/3/library/logging.html
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)

app = create_app()
app.secret_key = os.environ.get("SECRET_KEY")


# register the blueprint
app.register_blueprint(index)

# Register error handlers
register_error_handlers(app)

with app.app_context():
    # Create tables
    db.create_all()
    # TODO: NO SE SI LAS ESTOY LLAMANDO CONSTANTEMENTE TENGO QUE BUSCAR LA FORMA DE LLAMARLAS UNA SOLA VEZ
    roles.create_admin_role()
    roles.create_user_role()
    roles.create_admin_user()

app.app_context().push()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=5000)
