from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Request

from src.core.schemas.flashcard_stack_schemas import (
    FlashcardStackPublic,
    FlashcardStackSchema,
    FlashcardStackUpdate,
)
from src.database.query.query import Query
from src.di.dependencies import FlashcardStackServiceDependency

router = APIRouter(
    prefix='/flashcard_stacks',
    tags=['flashcard_stacks'],
)


@router.post(
    '', status_code=HTTPStatus.CREATED, response_model=FlashcardStackPublic
)
def create_flashcard_stack(
    request: Request,
    flashcard_stack: FlashcardStackSchema,
    flashcard_stack_service: FlashcardStackServiceDependency,
):
    result = flashcard_stack_service.add(flashcard_stack)
    return result


@router.get(
    '', status_code=HTTPStatus.OK, response_model=List[FlashcardStackPublic]
)
def get_flashcard_stacks(
    request: Request,
    flashcard_stack_service: FlashcardStackServiceDependency,
):
    query = Query(request.query_params)
    flashcard_stacks = flashcard_stack_service.get_all(query)
    return flashcard_stacks


@router.get(
    '/{flashcard_stack_id}',
    status_code=HTTPStatus.OK,
    response_model=FlashcardStackPublic,
)
def get_flashcard_stack_by_id(
    request: Request,
    flashcard_stack_id: int,
    flashcard_stack_service: FlashcardStackServiceDependency,
):
    flashcard_stack = flashcard_stack_service.get_by_id(flashcard_stack_id)
    return flashcard_stack


@router.patch(
    '/{flashcard_stack_id}',
    status_code=HTTPStatus.OK,
    response_model=FlashcardStackPublic,
)
def update_flashcard_stack(
    request: Request,
    flashcard_stack_id: int,
    flashcard_stack: FlashcardStackUpdate,
    flashcard_stack_service: FlashcardStackServiceDependency,
):
    updated_flashcard_stack = flashcard_stack_service.update(
        flashcard_stack_id, flashcard_stack
    )
    return updated_flashcard_stack


@router.delete('/{flashcard_stack_id}', status_code=HTTPStatus.NO_CONTENT)
def delete_flashcard_stack(
    request: Request,
    flashcard_stack_id: int,
    flashcard_stack_service: FlashcardStackServiceDependency,
):
    flashcard_stack_service.remove(flashcard_stack_id)
