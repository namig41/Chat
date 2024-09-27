from fastapi.routing import APIRouter

from logic.mediator import Mediator
from application.api.dependencies.containers import container

router = APIRouter(
    tags=['Chat'],
)

@router.post('/')
async def create_chat_handler():
    mediator = container.resolve(Mediator)