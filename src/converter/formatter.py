from ..models.journal_entry import JournalEntry
from ..models.note import Note

class MarkdownFormatter:
    @staticmethod
    def format_entry(entry: JournalEntry) -> Note:
        """Convert a journal entry to a markdown note"""
        date_str = entry.timestamp.strftime('%Y-%m-%d')
        title = f"Stoic Journal Entry - {date_str}"
        
        content = f"""---
date: {date_str}
tags: {', '.join(['stoic-journal'] + (entry.tags or []))}
mood: {entry.mood or 'Not recorded'}
---

# {title}

## Morning Reflection
{entry.morning_reflection or 'No morning reflection recorded'}

## Evening Reflection
{entry.evening_reflection or 'No evening reflection recorded'}

## Gratitude
{entry.gratitude or 'No gratitude recorded'}

## Daily Quote
> {entry.quote or 'No quote recorded'}

"""
        return Note(
            title=title,
            content=content,
            date=entry.timestamp,
            tags=['stoic-journal'] + (entry.tags or []),
            folder='Daily',
            filename=f"{date_str}_stoic_journal.md"
        )