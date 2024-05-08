# Importa el decorador dataclass desde el módulo dataclasses
from dataclasses import dataclass

# Importa la instancia db desde el módulo app, que parece ser un objeto de SQLAlchemy
from app import db


# Define una clase llamada UserData utilizando el decorador dataclass
@dataclass(init=False, repr=True, eq=True)
class UserData(
    db.Model
):  # Hereda de db.Model, lo que indica que es un modelo de base de datos
    __tablename__ = "users_data"  # Nombre de la tabla en la base de datos
    id: int = db.Column(
        db.Integer, primary_key=True, autoincrement=True
    )  # Columna de clave primaria
    firstname: str = db.Column(db.String(80), nullable=False)
    lastname: str = db.Column(db.String(80), nullable=False)
    phone: str = db.Column(
        db.String(120), nullable=False
    )  # Columna para el número de teléfono del usuario
    address: str = db.Column(
        db.String(120), nullable=False
    )  # Columna para la dirección del usuario
    city: str = db.Column(
        db.String(120), nullable=False
    )  # Columna para la ciudad del usuario
    country: str = db.Column(
        db.String(120), nullable=False
    )  # Columna para el país del usuario

    # Columna de clave externa para establecer la relación con la tabla 'users' (usuarios)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("users.id"))

    # Relación con la tabla 'User' (usuarios), establecida a través de la columna 'user_id'
    user = db.relationship("User", back_populates="data", uselist=False)
