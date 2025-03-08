from __future__ import annotations

from datetime import datetime
from typing import List

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models import table_registry


@table_registry.mapped_as_dataclass
class FlashcardStack:
    __tablename__ = 'flashcard_stacks'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    title: Mapped[str]
    flashcards: Mapped[List['Flashcard']] = relationship(  # noqa: F821
        back_populates='flashcard_stack',
    )
    main_language: Mapped[str]
    learning_language: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now(), onupdate=func.now()
    )
