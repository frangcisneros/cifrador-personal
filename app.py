from app import create_app, db
from app.routes.index import index
import os

import logging

# Ref: https://docs.python.org/3/library/logging.html
# ? buscar informacion sobre logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)

app = create_app()
app.secret_key = os.environ.get("SECRET_KEY")


# register the blueprint
app.register_blueprint(index)


with app.app_context():
    # create tables
    db.create_all()

app.app_context().push()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=5000)
