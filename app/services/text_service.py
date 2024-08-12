from app.models import Text, TextHistory
from app.repositories import TextHistoryRepository
from app import db


class TextService:
    """
    Edita el contenido de un objeto de texto.

    Args:
        text (Text): El objeto de texto a editar.
        new_content (str): El nuevo contenido del objeto de texto.

    Returns:
        Text: El objeto de texto modificado.
    """

    def edit_content(self, text: Text, new_content: str) -> Text:
        text_history_repository = TextHistoryRepository()
        text_history = text_history_repository.save(
            TextHistory(text_id=text.id, content=text.content)
        )
        text.content = new_content
        db.session.commit()
        return text
