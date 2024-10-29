from uuid import UUID
from fastapi import Depends
from punq import Container

from fastapi.routing import APIRouter
from fastapi.websockets import WebSocket

from infra.message_brokers.base import BaseMessageBroker
from logic.init import init_container
from settings.config import Config

router = APIRouter(
    tags=['chats'],
)

@router.websocket('/{chat_oid}/')
async def websocket_endpoint(
    chat_oid: UUID,
    websocket: WebSocket,
    container: Container = Depends(init_container)
):
    await websocket.accept()
    config: Config = container.resolve(Config)
    
    message_broker = container.resolve(BaseMessageBroker)

    try:
        async for consumed_message in await message_broker.start_consuming(
            topic=config.new_message_received_topic.format(chat_oid=chat_oid),
        ):
            await websocket.send_json(consumed_message)
    except Exception as e:
        raise e
    finally:
        await message_broker.stop_consuming(topic=chat_oid)
        await websocket.close(reason='Close websocket')
    
    
     