from dataclasses import dataclass
from app import db
from typing import List

from app.models.text import Text


@dataclass(init=False, repr=True, eq=True)
class TextHistory(db.Model):
    __tablename__ = "text_histories"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text_id: int = db.Column(db.Integer, db.ForeignKey("texts.id"), nullable=False)
    content: str = db.Column(db.String(120), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    def save(self) -> "TextHistory":
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find(cls, id: int) -> "TextHistory":
        return cls.query.get(id)

    @staticmethod
    def get_versions_of_text(text_id: int) -> List["TextHistory"]:
        # Obtiene todas las versiones de un texto específico.
        return (
            TextHistory.query.filter_by(text_id=text_id)
            .order_by(TextHistory.timestamp.desc())
            .all()
        )

    def change_to_version(self, version_id: int) -> None:
        # Cambia a una versión específica del texto.
        version = TextHistory.find(version_id)
        #! ESTO NO SE HACE
        from app.models.text import Text  # Importa dentro de la función o método

        if version:
            text = Text.find(self.text_id)
            text.content = version.content
            db.session.commit()
