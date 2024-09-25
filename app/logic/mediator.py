

from collections import defaultdict
from dataclasses import dataclass, field
from typing import Iterable
from domain.events.base import BaseEvent

from logic.commands.base import CT, CR, BaseCommand, CommandHandler
from logic.events.base import ET, ER, EventHandler
from logic.exceptions.mediator import CommandHandlersNotRegisteredException, EventHandlersNotRegisteredException


@dataclass(eq=False)
class Mediator:
    events_map: dict[type[BaseEvent], EventHandler] = field(
        default_factory=lambda: defaultdict[list],
        kw_only=True,
    )
    
    commands_map: dict[type[BaseCommand], CommandHandler] = field(
        default_factory=lambda: defaultdict[list],
        kw_only=True,
    )
    
    def register_event(self, event: ET, event_handler: EventHandler[ET, ER]):
        self.events_map[event.__class__].append(event_handler)
        
    def register_command(self, event: CT, command_handler: EventHandler[ET, ER]):
        self.events_map[event.__class__].append(command_handler)
        
    def handle_event(self, event: BaseEvent) -> Iterable[ER]:
        event_type = event.__class__
        handlers = self.events_map.get(event.__class__)
        
        if not handlers:
            raise EventHandlersNotRegisteredException(event_type)
        
        return [handler.handle(event) for handler in handlers]
    
    def handle_commands(self, command: BaseCommand) -> Iterable[CR]:
        command_type = command.__class__
        handlers = self.events_map.get(command.__class__)
        
        if not handlers:
            raise CommandHandlersNotRegisteredException(command_type)
        
        return [handler.handle(command) for handler in handlers]
            
            