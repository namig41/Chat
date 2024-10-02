from typing import Container
from fastapi import Depends, status
from fastapi import HTTPException
from fastapi.routing import APIRouter

from application.api.messages.schemas import CreateChatRequestSchema, CreateChatResponseSchema, CreateMessageRequestScheme, CreateMessageResponseScheme
from application.api.schemas import ErrorSchema
from domain.exceptions.base import ApplicationException
from logic.commands.messages import CreateChatCommand, CreateMessageCommand
from logic.init import init_container
from logic.mediator import Mediator

router = APIRouter(
    tags=['Chat'],
)

@router.post(
    '/',
    # response_model=CreateChatResponseSchema,
    status_code=status.HTTP_201_CREATED,
    description='Эндпоинт создает новый чат, если час с такими названием существует',
    responses={
        status.HTTP_201_CREATED: {'model': CreateChatResponseSchema},
        status.HTTP_400_BAD_REQUEST: {'model': ErrorSchema},
    },
)
async def create_chat_handler(scheme: CreateChatRequestSchema, container: Container = Depends(init_container)):
    mediator: Mediator = container.resolve(Mediator)
    
    try:
        chat, *_ = (await mediator.handle_command(CreateChatCommand(title=scheme.title)))
    except ApplicationException as exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'error': exception.message})
    
    return CreateChatResponseSchema.from_entiry(chat)

@router.post(
    '/{chat_oid}/messages',
    status_code=status.HTTP_201_CREATED,
    description='Ручка на добавление нового сообщения в чат с переданным ObjectID',
    responses={
        status.HTTP_201_CREATED: {'model': CreateMessageResponseScheme},
        status.HTTP_400_BAD_REQUEST: {'model': ErrorSchema}, 
    },
)
async def create_message_handler(
    chat_oid: str,
    scheme: CreateMessageRequestScheme,
    container: Container = Depends(init_container)
) -> CreateMessageResponseScheme:
    
    mediator: Mediator = container.resolve()
    
    try:
        message = await mediator.handle_command(CreateMessageCommand(text=scheme.text, chat_oid=chat_oid))
    except ApplicationException as exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'error': exception.message})
    
    return CreateMessageResponseScheme.from_entity(message)
        