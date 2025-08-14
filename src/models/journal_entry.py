from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List

@dataclass
class JournalEntry:
    timestamp: datetime
    morning_reflection: Optional[str] = None
    evening_reflection: Optional[str] = None
    gratitude: Optional[str] = None
    quote: Optional[str] = None
    mood: Optional[str] = None
    tags: List[str] = field(default_factory=list)  # Use field to set default for mutable types

