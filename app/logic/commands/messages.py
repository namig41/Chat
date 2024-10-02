from dataclasses import dataclass
from typing import Any, Text
from domain.entities.messages import Chat, Message
from domain.values.messages import Title
from infra.repositories.messages.base import BaseChatsRepository, BaseMessagesRepository
from logic.commands.base import BaseCommand, CommandHandler
from logic.exceptions.messages import ChatNotFoundException, ChatWithThatTitleAlreadyExisitsException

@dataclass(frozen=True)
class CreateChatCommand(BaseCommand):
    title: str
    chat_oid: str
    
@dataclass(frozen=True)
class CreateChatCommandHandler(CommandHandler[CreateChatCommand, Chat]): 
    chats_repository: BaseChatsRepository
    
    async def handle(self, command: CreateChatCommand) -> Chat:
        if await self.chats_repository.check_chat_exists_by_title(command.title):
            raise ChatWithThatTitleAlreadyExisitsException(command.title)
        title = Title(value=command.title)
        new_chat = Chat.create_chat(title=title)
        await self.chats_repository.add_chat(new_chat)
        return new_chat
    
@dataclass(frozen=True)
class CreateMessageCommand(BaseCommand):
    title: str
    chat_oid: str
    
@dataclass(frozen=True)
class CreateMessageCommandHandler(CommandHandler[CreateChatCommand, Chat]): 
    messages_repository: BaseMessagesRepository
    chats_repository: BaseChatsRepository
    
    
    async def handle(self, command: CreateChatCommand) -> Chat:
        if not (await self.chats_repository.get_chat_by_oid(oid=command.chat_oid)):
            raise ChatNotFoundException(command.chat_oid)
        
        message = Message(text=Text(value=command.text))
        await self.messages_repository.add_message(chat_oid=command.chat_oid, message=message)        
        