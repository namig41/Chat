from dataclasses import dataclass

from logic.exceptions.base import LogicExeption

@dataclass(frozen=True, eq=False)
class EventHandlersNotRegisteredException(LogicExeption):
    @property
    def message(self):
        return f'Не удалось найти обработчики для события: {self.event_type}'

@dataclass(frozen=True, eq=False)
class CommandHandlersNotRegisteredException(LogicExeption):
    @property
    def message(self):
        return f'Не удалось найти обработчики для команды: {self.command_type}'