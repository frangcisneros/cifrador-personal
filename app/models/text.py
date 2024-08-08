from dataclasses import dataclass
from app import db


@dataclass(init=False, repr=True, eq=True)
class BaseModel(db.Model):
    __abstract__ = True

    def to_json(self):
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }


@dataclass(init=False, repr=True, eq=True)
class Text(BaseModel):
    """
    Clase que representa un texto en la base de datos.
    Atributos:
    - id (int): Identificador único del texto.
    - content (str): Contenido del texto.
    - length (int): Longitud del texto.
    - language (str): Idioma del texto.
    - encrypted (bool): Indica si el texto está encriptado o no.
    - key (str): Clave de encriptación del texto.
    - user_id (int): Identificador del usuario al que pertenece el texto.
    - histories: Relación con los historiales de cambios del texto.
    Métodos:
    - __init__(self, content: str = "default text", language: str = "es"): Constructor de la clase.
    - to_json(self): Convierte el objeto a un diccionario JSON.
    """

    __tablename__ = "texts"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content: str = db.Column(db.String(120), nullable=False)
    length: int = db.Column(db.Integer, nullable=False)
    language: str = db.Column(db.String(120), nullable=False)
    encrypted: bool = db.Column(db.Boolean, default=False)
    key: str = db.Column(db.String(120), nullable=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    histories = db.relationship("TextHistory", backref="text", lazy=True)

    def __init__(self, content: str = "default text", language: str = "es"):
        """
        Inicializa una instancia de la clase Texto.

        Parámetros:
        - content (str): El contenido del texto. Por defecto es "default text".
        - language (str): El idioma del texto. Por defecto es "es".
        """
        self.content = content
        self.length = len(content)
        self.language = language
