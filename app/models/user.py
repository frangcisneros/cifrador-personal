from dataclasses import dataclass
from app import db
from app.models.relations import users_roles
from app.models.audit_mixin import AuditMixin
from app.models.soft_delete import SoftDeleteMixin


@dataclass
class User(SoftDeleteMixin, AuditMixin, db.Model):
    """
    Clase que representa un usuario en el sistema.
    Atributos:
    - id (int): Identificador único del usuario.
    - username (str): Nombre de usuario del usuario.
    - password (str): Contraseña del usuario.
    - email (str): Correo electrónico del usuario.
    - role_id (int): ID del rol del usuario.
    - roles (list): Lista de roles asociados al usuario.
    - users_rs (list): Lista de textos asociados al usuario.
    - data (UserData): Datos adicionales del usuario.
    Métodos:
    - __init__(username, password, email, data): Constructor de la clase User.
    - add_role(role): Agrega un rol al usuario.
    - remove_role(role): Remueve un rol del usuario.
    """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=True)

    roles = db.relationship("Role", secondary=users_roles, back_populates="users")
    users_rs = db.relationship("Text", backref="user", lazy=True)
    data = db.relationship(
        "UserData",
        uselist=False,
        back_populates="user",
        foreign_keys="[UserData.user_id]",
    )

    def __init__(self, username=None, password=None, email=None, data=None):
        self.data = data
        self.username = username
        self.password = password
        self.email = email

    def add_role(self, role):
        if role not in self.roles:
            self.roles.append(role)

    def remove_role(self, role):
        if role in self.roles:
            self.roles.remove(role)
