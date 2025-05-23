class JournalEntry:
    def __init__(self, title: str, content: str, date: str):
        self.title = title
        self.content = content
        self.date = date

    def __str__(self):
        return f"{self.date} - {self.title}\n{self.content}"

    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "date": self.date
        }