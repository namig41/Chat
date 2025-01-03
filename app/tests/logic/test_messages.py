import pytest
from faker import Faker

from domain.entities.messages import Chat
from domain.values.messages import Title
from infra.repositories.messages.base import BaseChatsRepository
from logic.commands.messages import CreateChatCommand
from logic.exceptions.messages import ChatWithThatTitleAlreadyExistsException
from logic.mediator.base import Mediator


@pytest.mark.asyncio
async def test_create_chat_command_success(
    chat_repository: BaseChatsRepository,
    mediator: Mediator,
    faker: Faker,
):

    chat: Chat
    chat, *_ = await mediator.handle_command(
        command=CreateChatCommand(title=faker.text()),
    )

    assert await chat_repository.check_chat_exists_by_title(
        title=chat.title.as_generic_type(),
    )


@pytest.mark.asyncio
async def test_create_chat_command_titile_already_exists(
    chat_repository: BaseChatsRepository,
    mediator: Mediator,
    faker: Faker,
):
    title_test = faker.text()
    chat = Chat(title=Title(title_test))
    await chat_repository.add_chat(chat)

    assert chat in chat_repository._saved_chats

    with pytest.raises(ChatWithThatTitleAlreadyExistsException):
        await mediator.handle_command(command=CreateChatCommand(title=title_test))

    assert len(chat_repository._saved_chats) == 1
