from app import create_app, db
from app.routes.index import index
import os

import logging

# TODO: leer el link de referencia sobre logging
# Ref: https://docs.python.org/3/library/logging.html
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)

app = create_app()
# TODO: probablemente pueda iniciar la secret key en el __init__ de la app
app.secret_key = os.environ.get("SECRET_KEY")


# TODO: cambiar el registro al __init__ de la app y ver si no se rompe nada
app.register_blueprint(index)


with app.app_context():
    db.create_all()

app.app_context().push()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=5000)
