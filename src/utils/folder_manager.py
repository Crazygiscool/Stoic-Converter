def create_folder(folder_path):
    """Create a folder at the specified path if it does not exist."""
    import os
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
    import os
    return [name for name in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, name))]