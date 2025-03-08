from src.core.services.flashcard_service import FlashcardService
from src.core.services.flashcard_stack_service import FlashcardStackService
from src.core.services.user_service import UserService
from src.di.container import container


def get_user_service() -> UserService:
    return container.user_service()


def get_flashcard_service() -> FlashcardService:
    return container.flashcard_service()


def get_flashcard_stack_service() -> FlashcardStackService:
    return container.flashcard_stack_service()
