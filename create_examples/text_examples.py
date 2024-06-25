# ------------------------------- importaciones ------------------------------ #
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import db, create_app
from app.models import Text
from app.repositories import TextRepository
from lorem_text import lorem


# ----------------------------- fin importaciones ---------------------------- #

# ---------------------------------------------------------------------------- #
#                  crea textos de ejemplo en la base de datos                  #
# ---------------------------------------------------------------------------- #

app = create_app()
app_context = app.app_context()
app_context.push()

text_repository = TextRepository()

for i in range(10):
    text = Text(content=lorem.words(i), language="es")
    text_repository.save(text)
