from functools import lru_cache
from punq import Container

from infra.repositories.messages import BaseChatRepository, MemoryChatRepository
from logic.commands.messages import CreateChatCommand, CreateChatCommandHandler
from logic.mediator import Mediator


def init_mediator(
    container: Container,
    mediator: Mediator,
    chat_repository: BaseChatRepository
):
    
     mediator.register_command(
         CreateChatCommand,
         [container.resolve(CreateChatCommandHandler)],
     )

@lru_cache(1)
def init_container():
    container = Container()
    container.register(BaseChatRepository, MemoryChatRepository)
    container.register(CreateChatCommandHandler)
    
    return container