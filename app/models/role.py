# Importa el decorador dataclass desde el módulo dataclasses
from dataclasses import dataclass
from .user import User

from app import db
from typing import List


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
