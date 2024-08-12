from app.models import UserData
from marshmallow import fields, Schema, post_load


class UserDataSchema(Schema):
    """
    Esquema para los datos del usuario.
    Atributos:
    - id (int): El ID del usuario.
    - firstname (str): El nombre del usuario.
    - lastname (str): El apellido del usuario.
    - address (str, opcional): La dirección del usuario.
    - city (str, opcional): La ciudad del usuario.
    - country (str, opcional): El país del usuario.
    - phone (str, opcional): El número de teléfono del usuario.
    Métodos:
    - make_data(data, **kwargs): Método decorador que crea una instancia de UserData a partir de los datos proporcionados.
    """

    id = fields.Integer(dump_only=True)
    firstname = fields.String(required=True, validate=fields.Length(min=1, max=80))
    lastname = fields.String(required=True, validate=fields.Length(min=1, max=80))
    address = fields.String(required=False, validate=fields.Length(min=1, max=120))
    city = fields.String(required=False, validate=fields.Length(min=1, max=120))
    country = fields.String(required=False, validate=fields.Length(min=1, max=120))
    phone = fields.String(required=False, validate=fields.Length(min=1, max=120))

    @post_load
    def make_data(self, data, **kwargs):
        """
        Método decorador que crea una instancia de UserData a partir de los datos proporcionados.
        Parámetros:
        - data (dict): Los datos del usuario.
        Retorna:
        - UserData: Una instancia de UserData creada a partir de los datos proporcionados.
        """
        return UserData(**data)
