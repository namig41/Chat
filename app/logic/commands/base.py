from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Generic, TypeVar


@dataclass(frozen=True)
class BaseCommand(ABC):
    ...
    
CT = TypeVar('CT', bound=BaseCommand)
CR = TypeVar('CR', bound=Any)

@dataclass(frozen=True)
class CommandHandler(ABC, Generic[CT]):
    @abstractmethod
    def handle(self, command: CT) -> CR:
        ...
        