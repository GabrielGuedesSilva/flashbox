from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from src.core.schemas.flashcard_schemas import FlashcardPublic


class FlashcardStackSchema(BaseModel):
    title: str
    flashcards: List[FlashcardPublic]
    main_language: str
    learning_language: str


class FlashcardStackPublic(BaseModel):
    id: int
    title: str
    flashcards: List[FlashcardPublic]
    main_language: str
    learning_language: str
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)


class FlashcardStackUpdate(BaseModel):
    title: Optional[str] = None
    flashcards: Optional[List[FlashcardPublic]] = None
    main_language: Optional[str] = None
    learning_language: Optional[str] = None
