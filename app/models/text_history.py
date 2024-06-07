from dataclasses import dataclass
from app import db
from typing import List


@dataclass(init=False, repr=True, eq=True)
class TextHistory(db.Model):
    __tablename__ = "text_histories"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text_id: int = db.Column(db.Integer, db.ForeignKey("texts.id"), nullable=False)
    content: str = db.Column(db.String(120), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    @staticmethod
    def get_versions_of_text(text_id: int) -> List["TextHistory"]:
        # Obtiene todas las versiones de un texto específico.
        return (
            TextHistory.query.filter_by(text_id=text_id)
            .order_by(TextHistory.timestamp.desc())
            .all()
        )
