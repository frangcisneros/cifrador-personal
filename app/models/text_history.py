# ------------------------------- importaciones ------------------------------ #
from dataclasses import dataclass
from app import db
from typing import List

# ----------------------------- fin importaciones ---------------------------- #


@dataclass(init=False, repr=True, eq=True)
class TextHistory(db.Model):
    __tablename__ = "text_histories"
    # ------------------------------ columnas tabla ------------------------------ #
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text_id: int = db.Column(db.Integer, db.ForeignKey("texts.id"), nullable=False)
    content: str = db.Column(db.String(120), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    # ---------------------------- fin columnas tabla ---------------------------- #
