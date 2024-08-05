# ------------------------------- importaciones ------------------------------ #
from cryptography.fernet import Fernet
from app.models import Text
from app.repositories import TextRepository
import base64

# ----------------------------- fin importaciones ---------------------------- #

# ------------------------------- repositorios ------------------------------- #
text_repository = TextRepository()
# ----------------------------- fin repositorios ----------------------------- #


class EncryptService:
    def encrypt_content(self, text: Text, key=None):
        if key is None:
            key = Fernet.generate_key()
        else:
            key = base64.urlsafe_b64encode((key.encode()).ljust(32, b"\0"))
        text.key = str(key.decode())
        f = Fernet(key)
        encrypted_content = f.encrypt(text.content.encode())
        text.content = encrypted_content.decode()
        text.encrypted = True
        text_repository.save(text)

    def decrypt_content(self, text: Text, decrypt_key) -> None:
        decrypt_key = base64.urlsafe_b64encode((decrypt_key.encode()).ljust(32, b"\0"))
        f = Fernet(decrypt_key)
        decrypted_content = f.decrypt(text.content.encode())
        text.content = decrypted_content.decode()
        text.encrypted = False
        text_repository.save(text)
