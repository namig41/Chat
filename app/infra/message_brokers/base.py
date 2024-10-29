from abc import ABC, abstractmethod
from dataclasses import dataclass

from aiokafka import AIOKafkaConsumer
from aiokafka.producer import AIOKafkaProducer


@dataclass
class BaseMessageBroker(ABC):
    @abstractmethod
    async def start(self):
        ...
        
    @abstractmethod
    async def stop(self):
        ... 
    
    @abstractmethod
    async def send_message(self, topic: str, value: bytes):
        ...
        
    @abstractmethod
    async def start_consuming(self, topic: str):
        ...
        
    @abstractmethod
    async def stop_consuming(self, topic: str):
        ...