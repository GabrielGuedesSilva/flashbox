from sqlalchemy.orm import registry

__all__ = ['table_registry', 'Flashcard', 'FlashcardStack', 'User']

table_registry = registry()

from src.database.models.flashcard import Flashcard
from src.database.models.flashcard_stack import FlashcardStack
from src.database.models.user import User
