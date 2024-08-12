from marshmallow import validate, fields, Schema


class ResponseSchema(Schema):
    """
    Esquema de respuesta para la API.

    Atributos:
    - message (str): El mensaje de la respuesta.
    - status_code (int): El código de estado de la respuesta.
    - data (dict, opcional): Los datos de la respuesta.
    """

    message = fields.String(required=True, validate=validate.Length(min=1))
    status_code = fields.Integer(required=True)
    data = fields.Dict(required=False)
