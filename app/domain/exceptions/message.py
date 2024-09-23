from dataclasses import dataclass

from domain.exceptions.base import ApplicationExcaption

@dataclass(eq=False)
class TextTooLongException(ApplicationExcaption):
    text: str
    
    @property
    def message(self):
        return f'Слишком длинный текст сообщения "{self.text[:255]}..."'
    
    