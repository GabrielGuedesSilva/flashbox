from __future__ import annotations

from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models import table_registry


@table_registry.mapped_as_dataclass
class Flashcard:
    __tablename__ = 'flashcards'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    title: Mapped[str]
    translation: Mapped[str]
    example: Mapped[str]
    flashcard_stack_id: Mapped[int] = mapped_column(
        ForeignKey('flashcard_stacks.id')
    )
    flashcard_stack: Mapped['FlashcardStack'] = relationship(  # noqa: F821
        back_populates='flashcards'
    )
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now(), onupdate=func.now()
    )
