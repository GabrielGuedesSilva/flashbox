from sqlalchemy.orm import Session

from src.core.schemas.flashcard_stack_schemas import FlashcardStackSchema
from src.database.models import FlashcardStack
from src.database.repositories.base_repository import BaseRepository


class FlashcardStackRepository(
    BaseRepository[FlashcardStack, FlashcardStackSchema]
):
    def __init__(self, db_connection: Session):
        super().__init__(db_connection, FlashcardStack)
