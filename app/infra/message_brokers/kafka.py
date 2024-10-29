from dataclasses import dataclass, field
from typing import Callable

from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
import orjson

from infra.message_brokers.base import BaseMessageBroker

@dataclass
class KafkaMessageBroker(BaseMessageBroker):
    producer: AIOKafkaProducer
    consumer: AIOKafkaConsumer
    consumer_map: dict[str, AIOKafkaConsumer] = field(
        default_factory=dict,
        kw_only=True,
    )
    
    async def start(self):
        await self.producer.start()
        
    async def stop(self):
        await self.producer.stop()
    
    async def send_message(self, key: bytes, topic: str, value: bytes):
        await self.producer.send(topic=topic, key=key, value=value)
        
    async def start_consuming(self, topic: str):
        await self.consumer.start()
        self.consumer.subscribe(topics=[topic])
        
        async for message in self.consumer:
            yield orjson(message.value)
                    
    async def stop_consuming(self, topic: str):
        self.consumer.unsubscribe()
        await self.consumer.stop()