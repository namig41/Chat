from dataclasses import dataclass, field
from uuid import uuid4

from domain.values.messages import Text

@dataclass
class Message:
    oid: str = field(
        default_factory=lambda: str(uuid4),
        kw_only=True
    )
    text: Text
    