from dataclasses import dataclass

from domain.events.messages import NewChatCreatedEvent
from logic.events.base import EventHandler
from logic.mediator.converters import convert_event_to_broker_message

@dataclass
class NewChatCreateEventHandler(EventHandler[NewChatCreatedEvent, None]):
    async def handle(self, event: NewChatCreatedEvent) -> None:
        await self.message_broker.send_message(
            topic=self.broker_topic,
            value=convert_event_to_broker_message(event=event)
        )
        print(f'Обработали событие {event.title}')