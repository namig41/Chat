from pydantic_settings import BaseSettings
from pydantic import Field

class Config(BaseSettings):
    mongodb_connection_uri: str = Field(alias='MONGO_DB_CONNECTION_URI')
    mongodb_chat_database: str = Field(default='chat', alias='MONGO_CHAT_DATABASE')
    mongodb_chat_collection: str = Field(default='chat', alias='MONGO_CHAT_COLLECTION')
    mongodb_messages_collection: str = Field(default='messages', alias='MONGODB_MESSAGES_COLLECTION')
    