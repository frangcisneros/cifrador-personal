from cryptography.fernet import Fernet
from app.models import Text
from app.repositories import TextRepository

text_repository = TextRepository()


# TODO: Cambiar los save() al repositorio de textos (que todavia no esta creado)
class EncryptService:
    def __init__(self):
        pass

    def encrypt_content(self, text: Text, key: bytes = Fernet.generate_key()) -> None:
        self.key = key
        f = Fernet(key)
        encrypted_content = f.encrypt(text.content.encode())
        text.content = encrypted_content.decode()
        text.encrypted = True
        text_repository.save(text)

    def decrypt_content(self, text: Text, key: bytes) -> None:
        f = Fernet(key)
        decrypted_content = f.decrypt(text.content.encode())
        text.content = decrypted_content.decode()
        text.encrypted = False
        text_repository.save(text)

    def change_content(self, text: Text, new_content: str) -> None:
        # Cambia el contenido del texto y guarda la versión anterior en TextHistory.
        #! ESTO NO SE HACE
        from app.models.text_history import (
            TextHistory,
        )  # Importa dentro de la función o método

        old_content = text.content
        text.content = new_content
        history = TextHistory(text_id=text.id, content=old_content)
        history.save()
        text_repository.save(text)
