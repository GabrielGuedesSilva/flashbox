from src.core.schemas.flashcard_stack_schemas import FlashcardStackSchema
from src.core.services.base_service import BaseService
from src.database.models import FlashcardStack
from src.database.repositories.flashcard_stack_repository import (
    FlashcardStackRepository,
)


class FlashcardStackService(BaseService[FlashcardStack, FlashcardStackSchema]):
    def __init__(self, flashcard_stack_repository: FlashcardStackRepository):
        super().__init__(flashcard_stack_repository, unique_fields=[])
