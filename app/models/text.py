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
    __tablename__ = "texts"  # Nombre de la tabla en la base de datos
    id: int = db.Column(
        db.Integer, primary_key=True, autoincrement=True
    )  # Columna de clave primaria
    content: str = db.Column(
        db.String(120), nullable=False
    )  # Columna para el texto del usuario
    length: int = db.Column(
        db.Integer, nullable=False
    )  # columna que indica el tamaño del texto
    language: str = db.Column(
        db.String(120), nullable=False
    )  # columna que indica el idioma del texto
    # Define la relación con TextHistory
    histories = db.relationship("TextHistory", backref="text", lazy=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    encrypted: bool = db.Column(db.Boolean, default=False)
    key: bytes = db.Column(db.LargeBinary, nullable=True)

    # TODO: Cambiar los save() al repositorio de textos (que todavia no esta creado)

    def save(self) -> "Text":
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()

    def __init__(self, content: str = "default text", language: str = "es"):
        self.content = content
        self.length = len(content)
        self.language = language

    @classmethod
    def find(cls, id: int) -> "Text":
        return cls.query.get(id)

    @classmethod
    def all(cls) -> List["Text"]:
        return cls.query.all()

    @classmethod
    def find_by(cls, **kwargs) -> List["Text"]:
        return cls.query.filter_by(**kwargs).all()
