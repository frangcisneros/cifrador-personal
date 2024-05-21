# Importa el decorador dataclass desde el módulo dataclasses
from dataclasses import dataclass
from .user import User

from app import db
from typing import List

from app.models.relations import users_roles
from app import db


# Define una clase llamada Role utilizando el decorador dataclass
@dataclass(init=False, repr=True, eq=True)
class Role(db.Model):
    __tablename__ = "roles"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(80), nullable=False)
    description: str = db.Column(db.String(255), nullable=False)
    user_role = db.relationship("User", backref="role", lazy=True)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self


# TODO: Implementar metodos para agregar, eliminar y istar usuarios
# TODO: Ver estos metodos del profesor
# class Role(db.Model):

#     __tablename__ = "roles"

#     id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)

#     name: str = db.Column(db.String(80), unique=True, nullable=False)

#     description: str = db.Column(db.String(255), nullable=False)

#     # Relacion Muchos a Muchos bidireccional con User

#     # Flask Web Development Capitulo: Database Relationships Revisited Pag 49,149

#     users = db.relationship("User", secondary=users_roles, back_populates="roles")

# def add_user(self, user):
#         if user not in self.users:
#             self.users.append(user)

# def remove_user(self, user):
#     if user in self.users:
#         self.users.remove(user)
