from cryptography.fernet import Fernet
from app.models import Text
from app.repositories import TextRepository
import base64


text_repository = TextRepository()


# TODO: separar logica encriptado y desencriptado y las key
# TODO: si el dia de mañana queremos encriptar archivos deberiamos usar el principio de Open/Closed para extender la función de encriptado
class EncryptService:

    def encrypt_content(self, text: Text, key=None):
        """
        Encripta el contenido de un objeto de texto utilizando una clave de encriptación.
        Parámetros:
        - text (Text): El objeto de texto cuyo contenido se va a encriptar.
        - key (str, opcional): La clave de encriptación a utilizar. Si no se proporciona, se generará una clave aleatoria.
        """
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
        """
        Desencripta el contenido de un objeto de texto utilizando una clave de desencriptación.
        Parámetros:
        - text (Text): El objeto de texto cuyo contenido se va a desencriptar.
        - decrypt_key (str): La clave de desencriptación a utilizar.
        """
        decrypt_key = base64.urlsafe_b64encode((decrypt_key.encode()).ljust(32, b"\0"))
        f = Fernet(decrypt_key)
        decrypted_content = f.decrypt(text.content.encode())
        text.content = decrypted_content.decode()
        text.encrypted = False
        text_repository.save(text)
