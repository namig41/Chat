
from dataclasses import dataclass
from domain.exceptions.base import ApplicationException

@dataclass(frozen=True, eq=False)
class LogicExeption(ApplicationException):
    @property
    def message(self):
        return 'В обработки запроса возникла ошибка'
    