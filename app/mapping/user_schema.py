from app.models.user import User
from marshmallow import validate, fields, Schema, post_load


class UserSchema(Schema):
    """
    Clase que define el esquema de usuario.
    Atributos:
    - id (int): Identificador del usuario.
    - username (str): Nombre de usuario del usuario.
    - email (str): Correo electrónico del usuario.
    - password (str): Contraseña del usuario.
    - data (UserDataSchema): Esquema anidado para los datos del usuario.
    Métodos:
    - make_user(data, **kwargs): Método decorador que crea una instancia de la clase User a partir de los datos proporcionados.
    """

    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    email = fields.String(required=True, validate=validate.Email())
    password = fields.String(load_only=True)
    data = fields.Nested("UserDataSchema")

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)
