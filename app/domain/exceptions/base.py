from dataclasses import dataclass

@dataclass(eq=False)
class ApplicationExcaption(Exception):
    
    @property
    def message(self):
        return 'Произошла ошибка приложения'