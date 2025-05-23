from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class JournalEntry:
    timestamp: datetime
    morning_reflection: Optional[str] = None
    evening_reflection: Optional[str] = None
    gratitude: Optional[str] = None
    quote: Optional[str] = None
    mood: Optional[str] = None
    tags: list[str] = None