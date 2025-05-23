import os
import shutil

class FolderManager:
    def __init__(self, base_dir: str):
        self.base_dir = base_dir
        self.folders = [
            "Daily",
            "Weekly_Reviews",
            "Monthly_Reviews",
            "Quotes",
            "Reflections",
            "Tags"
        ]

    def create_folder_structure(self) -> None:
        """Create the folder structure for Obsidian notes"""
        for folder in self.folders:
            path = os.path.join(self.base_dir, folder)
            os.makedirs(path, exist_ok=True)

    def clean_folders(self) -> None:
        """Clean all folders in the structure"""
        if os.path.exists(self.base_dir):
            shutil.rmtree(self.base_dir)
        self.create_folder_structure()

def create_folder(folder_path):
    """Create a folder at the specified path if it does not exist."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def organize_folders(base_path, journal_entries):
    """Organize folders for storing converted journal entries."""
    for entry in journal_entries:
        folder_name = entry.date.strftime("%Y-%m-%d")  # Example: Use entry date as folder name
        folder_path = os.path.join(base_path, folder_name)
        create_folder(folder_path)

def list_folders(base_path):
    """List all folders in the specified base path."""
    return [name for name in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, name))]