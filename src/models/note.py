from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List

@dataclass
class Note:
    title: str
    content: str
    date: datetime
    tags: List[str]
    folder: str
    filename: str