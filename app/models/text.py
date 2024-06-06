# ------------------------------- importaciones ------------------------------ #
from dataclasses import dataclass
from app import db

# ----------------------------- fin importaciones ---------------------------- #


@dataclass(init=False, repr=True, eq=True)
class Text(db.Model):
    __tablename__ = "texts"
    # --------------------------- columnas de la tabla --------------------------- #
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content: str = db.Column(db.String(120), nullable=False)
    length: int = db.Column(db.Integer, nullable=False)
    language: str = db.Column(db.String(120), nullable=False)
    encrypted: bool = db.Column(db.Boolean, default=False)
    key: bytes = db.Column(db.LargeBinary, nullable=True)
    # ------------------------------ claves foraneas ----------------------------- #
    user_id: int = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    # ----------------------------- fin clave foranea ---------------------------- #
    # ------------------------- fin columnas de la tabla ------------------------- #
    # -------------------------------- relaciones -------------------------------- #
    histories = db.relationship("TextHistory", backref="text", lazy=True)
    # ------------------------------ fin relaciones ------------------------------ #

    def __init__(self, content: str = "default text", language: str = "es"):
        self.content = content
        self.length = len(content)
        self.language = language
