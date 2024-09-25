from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from domain.entities.base import BaseEntity
from domain.events.messages import NewMessageReceivedEvent
from domain.values.messages import Title, Text

@dataclass(eq=False)
class Message(BaseEntity):
    
    oid: str = field(
        default_factory=lambda: str(uuid4()),
        kw_only=True
    )
    
    text: Text
    
    create_at: datetime = field(
        default_factory=datetime.now,
        kw_only=True
    )
    
@dataclass(eq=False)
class Chat(BaseEntity):
    oid: str = field(
        default_factory=lambda: str(uuid4()),
        kw_only=True
    )
    
    title: Title
    
    messages: set[Message] = field(
        default_factory=set,
        kw_only=True
    )
    
    create_at: datetime = field(
        default_factory=datetime.now,
        kw_only=True
    )
    
    def add_message(self, message: Message):
        self.messages.add(message)
        
        self.register_event(NewMessageReceivedEvent(
            message_text=message.text.as_generic_type(),
            chat_oid=self.oid,
            message_oid=message.oid,
        ))