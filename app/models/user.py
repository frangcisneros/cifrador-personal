# ------------------------------- importaciones ------------------------------ #
from dataclasses import dataclass
from .user_data import UserData
from app import db
from app.models.relations import users_roles
from app.models.audit_mixin import AuditMixin
from app.models.soft_delete import SoftDeleteMixin

# ----------------------------- fin importaciones ---------------------------- #


@dataclass(init=False, repr=True, eq=True)
class User(SoftDeleteMixin, AuditMixin, db.Model):
    __tablename__ = "users"
    # --------------------------- columnas de la tabla --------------------------- #
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username: str = db.Column(db.String(80), unique=True, nullable=False)
    password: str = db.Column("password", db.String(255), nullable=False)
    email: str = db.Column(db.String(120), unique=True, nullable=False)
    role_id: int = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=True)
    # ------------------------- fin columnas de la tabla ------------------------- #

    # -------------------------------- relaciones -------------------------------- #
    # * Relacion Muchos a Muchos bidireccional con Role
    roles = db.relationship("Role", secondary=users_roles, back_populates="users")
    # * Relación con la tabla 'Text' (texto), establecida a través de la propiedad 'user' en la clase Text
    users_rs = db.relationship("Text", backref="user", lazy=True)
    # * Relación con la tabla 'UserData' (datos de usuario), establecida a través de la propiedad 'user' en la clase UserData
    data = db.relationship(
        "UserData",
        uselist=False,
        back_populates="user",
        foreign_keys="[UserData.user_id]",
    )
    # ------------------------------ fin relaciones ------------------------------ #

    def __init__(self, user_data: UserData):
        self.data = user_data

    def add_role(self, role):
        if role not in self.roles:
            self.roles.append(role)

    def remove_role(self, role):
        if role in self.roles:
            self.roles.remove(role)
