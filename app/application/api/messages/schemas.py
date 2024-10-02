from pydantic import BaseModel

from domain.entities.messages import Chat, Message

class CreateChatRequestSchema(BaseModel):
    title: str
    
class CreateChatResponseSchema(BaseModel):
    oid: str
    title: str
    
    @classmethod
    def from_entiry(cls, chat: Chat) -> 'CreateChatResponseSchema':
        return cls(
            oid=chat.oid,
            title=chat.title.as_generic_type()
        )
    
class CreateMessageRequestScheme(BaseModel):
    text: str
    
class CreateMessageResponseScheme(BaseModel):
    text: str
    oid: str

    @classmethod
    def from_entiry(cls, message: Message) -> 'CreateMessageResponseScheme':
        return cls(
            text=message.text,
            oid=message.oid
        )