from dataclasses import dataclass, field
from typing import Optional, Dict


@dataclass
class ResponseMessage:
    message: str
    status_code: int
    data: Optional[Dict] = None


@dataclass
class ResponseBuilder:
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
