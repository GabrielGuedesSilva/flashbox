from src.core.schemas.flashcard_schemas import FlashcardSchema
from src.core.services.base_service import BaseService
from src.database.models import Flashcard
from src.database.repositories.flashcard_repository import FlashcardRepository


class FlashcardService(BaseService[Flashcard, FlashcardSchema]):
    def __init__(self, flashcard_repository: FlashcardRepository):
        super().__init__(flashcard_repository, unique_fields=[])
