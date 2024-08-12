from dataclasses import dataclass, field
from typing import Optional, Dict


@dataclass
class ResponseMessage:
    message: str
    status_code: int
    data: Optional[Dict] = None


@dataclass
class ResponseBuilder:
    """
    Clase ResponseBuilder: Construye un objeto ResponseMessage con los atributos proporcionados.
    Atributos:
        _message (str): El mensaje de la respuesta.
        _status_code (int): El código de estado de la respuesta.
        _data (Dict): Los datos asociados a la respuesta.
    Métodos:
        set_message(message: str) -> ResponseBuilder:
            Establece el mensaje de la respuesta y devuelve una instancia de ResponseBuilder.
        set_status_code(status_code: int) -> ResponseBuilder:
            Establece el código de estado de la respuesta y devuelve una instancia de ResponseBuilder.
        set_data(data: Dict) -> ResponseBuilder:
            Establece los datos asociados a la respuesta y devuelve una instancia de ResponseBuilder.
        build() -> ResponseMessage:
            Construye y devuelve un objeto ResponseMessage con los atributos proporcionados.
    Raises:
        ValueError: Se produce si no se proporciona el mensaje o el código de estado.
    """

    _message: Optional[str] = field(default=None, init=False)
    _status_code: Optional[int] = field(default=None, init=False)
    _data: Optional[Dict] = field(default=None, init=False)

    def set_message(self, message: str):
        self._message = message
        return self

    def set_status_code(self, status_code: int):
        self._status_code = status_code
        return self

    def set_data(self, data: Dict):
        self._data = data
        return self

    def build(self):
        if self._message is None or self._status_code is None:
            raise ValueError("Message and status code must be provided")

        return ResponseMessage(
            message=self._message,
            status_code=self._status_code,
            data=self._data,
        )
