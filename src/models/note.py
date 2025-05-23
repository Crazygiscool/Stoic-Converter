class Note:
    def __init__(self, title: str, content: str, date: str):
        self.title = title
        self.content = content
        self.date = date

    def save(self, folder_path: str):
        """Saves the note to a file in the specified folder."""
        file_path = f"{folder_path}/{self.title}.md"
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"# {self.title}\n\n")
            file.write(f"Date: {self.date}\n\n")
            file.write(self.content)

    @staticmethod
    def retrieve(file_path: str):
        """Retrieves a note from a file."""
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            title = lines[0].strip('# ').strip()
            date_line = lines[1].strip()
            date = date_line.split(": ")[1]
            content = ''.join(lines[3:])
            return Note(title, content, date)