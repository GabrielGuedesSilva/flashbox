from sqlalchemy.orm import Session

from src.core.schemas.flashcard_schemas import FlashcardSchema
from src.database.models import Flashcard
from src.database.repositories.base_repository import BaseRepository


class FlashcardRepository(BaseRepository[Flashcard, FlashcardSchema]):
    def __init__(self, db_connection: Session):
        super().__init__(db_connection, Flashcard)
