from dataclasses import dataclass, field
from datetime import datetime
from typing import List

@dataclass
class Note:
    title: str
    content: str
    date: datetime
    tags: List[str] = field(default_factory=list)  # Default to an empty list
    folder: str = "Uncategorized"  # Default folder name
    filename: str = ""  # Default to an empty string; can be set later

