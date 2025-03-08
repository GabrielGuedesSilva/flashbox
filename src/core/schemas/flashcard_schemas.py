from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class FlashcardSchema(BaseModel):
    title: str
    translation: str
    example: str


class FlashcardPublic(BaseModel):
    id: int
    title: str
    translation: str
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)


class FlashcardUpdate(BaseModel):
    title: Optional[str] = None
    translation: Optional[str] = None
