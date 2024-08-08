from dataclasses import dataclass
from app import db


@dataclass(init=False, repr=True, eq=True)
class TextHistory(db.Model):
    """
    Clase que representa el historial de texto.
    Atributos:
    - id (int): Identificador único del historial de texto.
    - text_id (int): Identificador del texto asociado al historial.
    - content (str): Contenido del historial de texto.
    - timestamp (DateTime): Marca de tiempo del historial de texto.
    """

    __tablename__ = "text_histories"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text_id: int = db.Column(db.Integer, db.ForeignKey("texts.id"), nullable=False)
    content: str = db.Column(db.String(120), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
