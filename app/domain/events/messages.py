from dataclasses import dataclass
from typing import ClassVar
from domain.events.base import BaseEvent

@dataclass
class NewMessageReceivedEvent(BaseEvent):
    title: ClassVar[str] = 'New Message Recieved'
    
    message_text: str
    message_oid: str
    chat_oid: str
    
@dataclass
class NewChatCreatedEvent(BaseEvent):
    title: ClassVar[str] = 'New Message Created'
    
    chat_oid: str
    chat_title: str