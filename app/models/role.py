from dataclasses import dataclass
from app.models.relations import users_roles
from app import db


@dataclass(init=False, repr=True, eq=True)
class Role(db.Model):
    """
    Clase Role
    Representa un rol en el sistema.
    Atributos:
    - id (int): Identificador único del rol.
    - name (str): Nombre del rol.
    - description (str): Descripción del rol.
    - users (list): Lista de usuarios asociados al rol.
    Métodos:
    - add_user(user): Agrega un usuario a la lista de usuarios asociados al rol.
    - remove_user(user): Remueve un usuario de la lista de usuarios asociados al rol.
    """

    __tablename__ = "roles"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(80), unique=True, nullable=False)
    description: str = db.Column(db.String(255), nullable=False)
    users = db.relationship("User", secondary=users_roles, back_populates="roles")

    # TODO: Implementar metodos para agregar, eliminar y listar usuarios
    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
