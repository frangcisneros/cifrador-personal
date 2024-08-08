from dataclasses import dataclass
from app import db
from app.models.audit_mixin import AuditMixin
from app.models.soft_delete import SoftDeleteMixin


@dataclass(init=False, repr=True, eq=True)
class UserData(db.Model, AuditMixin, SoftDeleteMixin):
    """
    Clase UserData
    Representa los datos de un usuario en la aplicación.
    Atributos:
    - id (int): Identificador único del usuario.
    - firstname (str): Nombre del usuario.
    - lastname (str): Apellido del usuario.
    - phone (str): Número de teléfono del usuario.
    - address (str): Dirección del usuario.
    - city (str): Ciudad del usuario.
    - country (str): País del usuario.
    - user_id (int): Identificador del usuario asociado.
    - user (User): Objeto de la clase User asociado al usuario.
    - profile_id (int): Identificador del perfil asociado.
    - profile (Profile): Objeto de la clase Profile asociado al usuario.
    Métodos:
    - __init__(self, firstname: str = None, lastname: str = None, phone: str = None, address: str = None, city: str = None, country: str = None, profile=None): Constructor de la clase UserData.
    """

    __tablename__ = "users_data"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname: str = db.Column(db.String(80), nullable=False)
    lastname: str = db.Column(db.String(80), nullable=False)
    phone: str = db.Column(db.String(120), nullable=False)
    address: str = db.Column(db.String(120), nullable=False)
    city: str = db.Column(db.String(120), nullable=False)
    country: str = db.Column(db.String(120), nullable=False)

    user_id = db.Column("user_id", db.Integer, db.ForeignKey("users.id"))

    user = db.relationship(
        "User", back_populates="data", foreign_keys=[user_id], uselist=False
    )

    profile_id = db.Column("profile_id", db.Integer, db.ForeignKey("profiles.id"))
    profile = db.relationship(
        "Profile", back_populates="data", foreign_keys=[profile_id]
    )

    def __init__(
        self,
        firstname: str,
        lastname: str,
        phone: str,
        address: str,
        city: str,
        country: str,
        profile=None,
    ):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.address = address
        self.city = city
        self.country = country
        self.profile = profile
