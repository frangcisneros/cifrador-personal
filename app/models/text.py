# Importa el decorador dataclass desde el módulo dataclasses
from dataclasses import dataclass

# Importa la instancia db desde el módulo app, que parece ser un objeto de SQLAlchemy
from app import db
from typing import List


# Definimos una clase llamada Text utilizando el decorador dataclass
@dataclass(init=False, repr=True, eq=True)
class Text(
    db.Model
):  # Hereda de db.Model, lo que indica que es un modelo de base de datos
    __tablename__ = "texts"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content: str = db.Column(db.String(120), nullable=False)
    length: int = db.Column(db.Integer, nullable=False)
    language: str = db.Column(db.String(120), nullable=False)
    # Define la relación con TextHistory
    histories = db.relationship("TextHistory", backref="text", lazy=True)

    # relacion uno a muchos con User

    # foreign key to users
    user_id: int = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)

    encrypted: bool = db.Column(db.Boolean, default=False)
    key: bytes = db.Column(db.LargeBinary, nullable=True)

    def __init__(self, content: str = "default text", language: str = "es"):
        self.content = content
        self.length = len(content)
        self.language = language
