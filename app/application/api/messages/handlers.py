from fastapi import Depends, status
from fastapi import HTTPException
from fastapi.routing import APIRouter

from application.api.messages.schemas import CreateChatRequestSchema, CreateChatResponseSchema
from application.api.schemas import ErrorSchema
from domain.exceptions.base import ApplicationException
from logic.commands.messages import CreateChatCommand
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
        status.HTTP_400_BAD_REQUEST: {'model': ErrorSchema} 
    },
)
async def create_chat_handler(scheme: CreateChatRequestSchema, container=Depends(init_container)):
    mediator: Mediator = container.resolve(Mediator)
    
    try:
        chat, *_ = (await mediator.handle_command(CreateChatCommand(title=scheme.title)))
    except ApplicationException as exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'error': exception.message})
    
    return CreateChatResponseSchema.from_entiry(chat)