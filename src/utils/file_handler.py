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
    import os
    return os.path.isfile(file_path)

def create_directory(directory_path):
    """Creates a directory if it doesn't exist."""
    import os
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)