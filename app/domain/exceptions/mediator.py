from dataclasses import dataclass

from logic.exceptions.base import LogicExeption


@dataclass(eq=False)
class EventHandlersNotRegisteredException(LogicExeption):
    event_type: type

    @property
    def message(self):
        return f"Не удалось найти обработчики для события: {self.event_type}"


@dataclass(eq=False)
class CommandHandlerNotRegisteredException(LogicExeption):
    command_type: type

    @property
    def message(self):
        return f"Не удалось найти обработчики для команды: {self.command_type}"
