from dependency_injector import containers, providers

from core.services.flashcard_service import FlashcardService
from core.services.flashcard_stack_service import FlashcardStackService
from src.core.services.user_service import UserService
from src.database.database_connection import DatabaseConnection
from src.database.repositories.flashcard_repository import FlashcardRepository
from src.database.repositories.flashcard_stack_repository import (
    FlashcardStackRepository,
)
from src.database.repositories.user_repository import UserRepository
from src.utils.settings import Settings


class Container(containers.DeclarativeContainer):
    # Config
    settings = providers.Singleton(Settings)

    # Database
    db_connection = providers.Singleton(
        DatabaseConnection,
        database_url=settings.provided.DATABASE_URL,
    )

    # Repositories
    user_repository = providers.Singleton(
        UserRepository, db_connection=db_connection
    )
    flashcard_repository = providers.Singleton(
        FlashcardRepository, db_connection=db_connection
    )
    flashcard_stack_repository = providers.Singleton(
        FlashcardStackRepository, db_connection=db_connection
    )

    # Services
    user_service = providers.Factory(
        UserService, user_repository=user_repository
    )
    flashcard_service = providers.Factory(
        FlashcardService, flashcard_repository=flashcard_repository
    )
    flashcard_stack_service = providers.Factory(
        FlashcardStackService,
        flashcard_stack_repository=flashcard_stack_repository,
    )


container = Container()
