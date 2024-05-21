# Importa el decorador dataclass desde el módulo dataclasses
from dataclasses import dataclass

# Importa la clase UserData desde el archivo user_data.py en el mismo directorio
from .user_data import UserData

# Importa la instancia db desde el módulo app, que parece ser un objeto de SQLAlchemy
from app import db
from typing import List
from app.models.relations import users_roles


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
    password: str = db.Column("password", db.String(255), nullable=False)
    email: str = db.Column(db.String(120), unique=True, nullable=False)
    # Relacion Uno a Uno bidireccional con UserData
    role_id: int = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=True)

    # Relación con la tabla 'Text' (texto), establecida a través de la propiedad 'user' en la clase Text
    users_rs = db.relationship("Text", backref="user", lazy=True)

    # Relación con la tabla 'UserData' (datos de usuario), establecida a través de la propiedad 'user' en la clase UserData
    data = db.relationship("UserData", uselist=False, back_populates="user")  # type: ignore

    # TODO: Cambios del profesor en roles
    # Relacion Muchos a Muchos bidireccional con Role
    # Flask Web Development Capitulo: Database Relationships Revisited Pag 49,149
    # roles = db.relationship("Role", secondary=users_roles, back_populates='users')

    # Constructor de la clase User, que puede recibir un objeto UserData opcionalmente
    def __init__(self, user_data: UserData):
        self.data = user_data

    def add_role(self, role):
        if role not in self.roles:
            self.roles.append(role)

    def remove_role(self, role):
        if role in self.roles:
            self.roles.remove(role)

    # def save(self):
    #     db.session.add(self)
    #     db.session.commit()
    #     return self

    # def delete(self) -> None:
    #     db.session.delete(self)
    #     db.session.commit()

    # @classmethod
    # def all(cls) -> List["User"]:
    #     return cls.query.all()

    # @classmethod
    # def find(cls, id: int) -> "User":
    #     return db.session.get(cls, id)

    # @classmethod
    # def find_by(cls, **kwargs) -> List["User"]:
    #     return cls.query.filter_by(**kwargs).all()
