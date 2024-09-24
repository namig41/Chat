from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

@dataclass(eq=False)
class BaseEntity(ABC):
    oid: str = field(
        default_factory=lambda: str(uuid4()),
        kw_only=True
    )
    
    create_at: datetime = field(
        default_factory=datetime.now,
        kw_only=True
    )
    
    def __hash__(self) -> int:
        return hash(self.oid)
    

    def __eq__(self, _value: 'BaseEntity') -> bool:
        return self.oid == _value.oid