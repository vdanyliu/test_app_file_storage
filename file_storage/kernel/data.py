from dataclasses import dataclass, field
from io import BytesIO
from uuid import uuid4


@dataclass
class InputFile:
    file_name: str
    data: BytesIO
    id: str = field(default_factory=lambda: uuid4().hex)
