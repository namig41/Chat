from pydantic import BaseModel

from domain.entities.messages import Chat

class CreateChatRequestSchema(BaseModel):
    title: str
    
class CreateChatResponseSchema(BaseModel):
    oid: str
    title: str
    
    @staticmethod
    def from_entiry(csl, chat: Chat) -> 'CreateChatResponseSchema':
        return CreateChatResponseSchema(
            oid=chat.oid,
            title=chat.title.as_generic_type()
        )