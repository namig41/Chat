
from dataclasses import dataclass
from domain.exceptions.base import ApplicationException

@dataclass(eq=False)
class LogicExeption(ApplicationException):
    @property
    def message(self):
        return 'В обработки запроса возникла ошибка'
    