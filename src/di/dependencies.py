from typing import Annotated

from fastapi import Depends

from src.core.services.flashcard_service import FlashcardService
from src.core.services.flashcard_stack_service import FlashcardStackService
from src.core.services.user_service import UserService
from src.di.providers import (
    get_flashcard_service,
    get_flashcard_stack_service,
    get_user_service,
)

UserServiceDependency = Annotated[UserService, Depends(get_user_service)]
FlashcardServiceDependency = Annotated[
    FlashcardService, Depends(get_flashcard_service)
]
FlashcardStackServiceDependency = Annotated[
    FlashcardStackService, Depends(get_flashcard_stack_service)
]
