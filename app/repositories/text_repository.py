from typing import List
from app.models import Text, TextHistory
from app import db


class TextRepository:
    """
    Clase que representa un repositorio de texto.
    Métodos:
    - save(text: Text) -> Text: Guarda un objeto de texto en la base de datos.
    - delete(text: Text) -> None: Elimina un objeto de texto de la base de datos.
    - find(id: int): Busca un objeto de texto por su ID en la base de datos.
    - all() -> List["Text"]: Obtiene todos los objetos de texto de la base de datos.
    - find_by(**kwargs) -> List["Text"]: Busca objetos de texto en la base de datos según los criterios proporcionados.
    Atributos:
    - No hay atributos definidos en esta clase.
    """

    def save(self, text: Text) -> Text:
        db.session.add(text)
        db.session.commit()
        return text

    def delete(self, text: Text) -> None:
        db.session.delete(text)
        db.session.commit()

    def find(self, id: int):
        return db.session.query(Text).filter(Text.id == id).one()

    def all(self) -> List["Text"]:
        texts = db.session.query(Text).all()
        return texts

    def find_by(self, **kwargs) -> List["Text"]:
        return db.session.query(Text).filter_by(**kwargs).all()
