from app.models import Text, TextHistory
from app.repositories import TextRepository, TextHistoryRepository
from app import db


class TextService:
    def edit_content(self, text: Text, new_content: str) -> Text:
        text_history_repository = TextHistoryRepository()
        text_history = text_history_repository.save(
            TextHistory(text_id=text.id, content=text.content)
        )
        text.content = new_content
        db.session.commit()
        return text
