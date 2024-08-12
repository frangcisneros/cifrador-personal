from typing import List
from app.models import TextHistory
from app import db


class TextHistoryRepository:
    """
    Repositorio para almacenar y recuperar objetos TextHistory.
    Métodos:
    - save(text_history: TextHistory) -> TextHistory: Guarda un objeto TextHistory en la base de datos.
    - delete(text_history: TextHistory) -> None: Elimina un objeto TextHistory de la base de datos.
    - find(id: int): Recupera un objeto TextHistory de la base de datos por su ID.
    - all() -> List[TextHistory]: Recupera todos los objetos TextHistory de la base de datos.
    - find_by(**kwargs) -> List[TextHistory]: Recupera objetos TextHistory de la base de datos que coinciden con los criterios proporcionados.
    """

    def save(self, text_history: TextHistory) -> TextHistory:
        db.session.add(text_history)
        db.session.commit()
        return text_history

    def delete(self, text_history: TextHistory) -> None:
        db.session.delete(text_history)
        db.session.commit()

    def find(self, id: int):
        return db.session.query(TextHistory).filter(TextHistory.id == id).one()

    def all(self) -> List["TextHistory"]:
        text_histories = db.session.query(TextHistory).all()
        return text_histories

    def find_by(self, **kwargs) -> List["TextHistory"]:
        return db.session.query(TextHistory).filter_by(**kwargs).all()
