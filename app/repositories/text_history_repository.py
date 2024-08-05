from typing import List
from app.models import TextHistory
from app import db


class TextHistoryRepository:
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
