from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

from domain.events.base import BaseEvent

@dataclass(frozen=True)
class BaseQuery(ABC):
    ...
    
QT = TypeVar('QT', bound=BaseEvent)
QR = TypeVar('QR', bound=Any)

@dataclass(frozen=True)
class BaseQueryHandler(ABC, Generic[QT, QR]):
    @abstractmethod
    async def handle(self, command: QT) -> QR:
        ...