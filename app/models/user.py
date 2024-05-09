# Importa el decorador dataclass desde el módulo dataclasses
from dataclasses import dataclass

# Importa la clase UserData desde el archivo user_data.py en el mismo directorio
from .user_data import UserData

# Importa la instancia db desde el módulo app, que parece ser un objeto de SQLAlchemy
from app import db
from typing import List


# Define una clase llamada User utilizando el decorador dataclass
@dataclass(init=False, repr=True, eq=True)
class User(
    db.Model
):  # Hereda de db.Model, lo que indica que es un modelo de base de datos
    __tablename__ = "users"  # Nombre de la tabla en la base de datos
    id: int = db.Column(
        db.Integer, primary_key=True, autoincrement=True
    )  # Columna de clave primaria
    username: str = db.Column(
        db.String(80), unique=True, nullable=False
    )  # Columna para el nombre de usuario
    password: str = db.Column(
        db.String(120), nullable=False
    )  # Columna para la contraseña del usuario
    email: str = db.Column(
        db.String(120), unique=True, nullable=False
    )  # Columna para el correo electrónico del usuario
    users_rs = db.relationship("Text", backref="user", lazy=True)

    # Relación con la tabla 'UserData' (datos de usuario), establecida a través de la propiedad 'user' en la clase UserData
    data = db.relationship("UserData", uselist=False, back_populates="user")  # type: ignore

    # Constructor de la clase User, que puede recibir un objeto UserData opcionalmente
    def __init__(self, user_data: UserData = None):
        self.data = user_data

    """
    Aplico el patrón Active Record https://www.martinfowler.com/eaaCatalog/activeRecord.html, donde el modelo se encarga de la persistencia de los datos.
    Este patrón es muy útil para aplicaciones pequeñas y medianas, pero no es recomendable para aplicaciones grandes.
    Puede llegar a contradecir los principios SOLID http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod, ya que el modelo tiene responsabilidades de persistencia y de negocio.
    """

    def save(self) -> "User":
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()

    # ? ¿Lo necesito?
    # @classmethod
    # def all(cls) -> List["User"]:
    #     return cls.query.all()

    @classmethod
    def find(cls, id: int) -> "User":
        return cls.query.get(id)

    # ? ¿Lo necesito?
    # @classmethod
    # def find_by(cls, **kwargs) -> List["User"]:
    #     return cls.query.filter_by(**kwargs).all()
