import os
from ..models.note import Note

def read_file(file_path):
    """Reads the content of a file and returns it."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_path, content):
    """Writes content to a file, creating it if it doesn't exist."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def append_to_file(file_path, content):
    """Appends content to a file."""
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(content)

def file_exists(file_path):
    """Checks if a file exists."""
    return os.path.isfile(file_path)

def create_directory(directory_path):
    """Creates a directory if it doesn't exist."""
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

class FileHandler:
    def __init__(self, base_dir: str):
        self.base_dir = base_dir

    def save_note(self, note: Note) -> None:
        """Save a note to the appropriate folder"""
        folder_path = os.path.join(self.base_dir, note.folder)
        os.makedirs(folder_path, exist_ok=True)
        
        file_path = os.path.join(folder_path, note.filename)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(note.content)