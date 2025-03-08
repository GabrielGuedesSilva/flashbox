from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Request

from src.core.schemas.flashcard_schemas import (
    FlashcardPublic,
    FlashcardSchema,
    FlashcardUpdate,
)
from src.database.query.query import Query
from src.di.dependencies import FlashcardServiceDependency

router = APIRouter(
    prefix='/flashcards',
    tags=['flashcards'],
)


@router.post(
    '', status_code=HTTPStatus.CREATED, response_model=FlashcardPublic
)
def create_flashcard(
    request: Request,
    flashcard: FlashcardSchema,
    flashcard_service: FlashcardServiceDependency,
):
    result = flashcard_service.add(flashcard)
    return result


@router.get(
    '', status_code=HTTPStatus.OK, response_model=List[FlashcardPublic]
)
def get_flashcards(
    request: Request,
    flashcard_service: FlashcardServiceDependency,
):
    query = Query(request.query_params)
    flashcards = flashcard_service.get_all(query)
    return flashcards


@router.get(
    '/{flashcard_id}',
    status_code=HTTPStatus.OK,
    response_model=FlashcardPublic,
)
def get_flashcard_by_id(
    request: Request,
    flashcard_id: int,
    flashcard_service: FlashcardServiceDependency,
):
    flashcard = flashcard_service.get_by_id(flashcard_id)
    return flashcard


@router.patch(
    '/{flashcard_id}',
    status_code=HTTPStatus.OK,
    response_model=FlashcardPublic,
)
def update_flashcard(
    request: Request,
    flashcard_id: int,
    flashcard: FlashcardUpdate,
    flashcard_service: FlashcardServiceDependency,
):
    updated_flashcard = flashcard_service.update(flashcard_id, flashcard)
    return updated_flashcard


@router.delete('/{flashcard_id}', status_code=HTTPStatus.NO_CONTENT)
def delete_flashcard(
    request: Request,
    flashcard_id: int,
    flashcard_service: FlashcardServiceDependency,
):
    flashcard_service.remove(flashcard_id)
