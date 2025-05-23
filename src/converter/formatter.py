class Formatter:
    def __init__(self):
        pass

    def format_entry(self, journal_entry):
        """
        Formats a single journal entry into the Obsidian note format.
        
        Args:
            journal_entry (JournalEntry): The journal entry to format.
        
        Returns:
            str: The formatted note as a string.
        """
        formatted_note = f"# {journal_entry.title}\n\n"
        formatted_note += f"Date: {journal_entry.date}\n\n"
        formatted_note += f"{journal_entry.content}\n"
        return formatted_note

    def format_entries(self, journal_entries):
        """
        Formats multiple journal entries into a list of Obsidian notes.
        
        Args:
            journal_entries (list): A list of JournalEntry objects.
        
        Returns:
            list: A list of formatted notes as strings.
        """
        return [self.format_entry(entry) for entry in journal_entries]