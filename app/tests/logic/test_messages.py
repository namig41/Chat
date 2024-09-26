import pytest
from domain.entities.messages import Chat
from domain.values.messages import Title
from infra.repositories.messages import BaseChatRepository
from logic.commands.messages import CreateChatCommand
from logic.mediator import Mediator


@pytest.mark.asyncio
async def test_create_chat_command_success(
    chat_repository: BaseChatRepository,
    mediator: Mediator,
):
    chat: Chat = next(await mediator.handle_commands(CreateChatCommand(title=Title("Test Create"))))[0]
    
    assert chat_repository.check_chat_exists_by_title(title=chat.title.as_generic_type())
     