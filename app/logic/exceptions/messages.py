from dataclasses import dataclass
from logic.exceptions.base import LogicExeption


@dataclass(eq=False)
class ChatWithThatTitleAlreadyExisitsException(LogicExeption):
    title: str
    
    @property
    def message(self):
        return f'Чат с таким названием существет {self.title}'