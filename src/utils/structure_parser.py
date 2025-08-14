import os

def list_folder_structure(startpath: str, output_file: str = None):
    """Recursively list the folder structure starting from the given path.
    
    Args:
        startpath (str): The path to start listing the folder structure.
        output_file (str, optional): The file to write the output to. If None, print to console.
    """
    output = []  # List to hold the output lines

    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)  # Count the depth of the current directory
        indent = ' ' * 4 * (level)  # Indentation for visual hierarchy
        output.append(f"{indent}{os.path.basename(root)}/")  # Add the directory name to output
        subindent = ' ' * 4 * (level + 1)  # Indentation for files
        for f in files:
            output.append(f"{subindent}{f}")  # Add the file name to output

    # Print to console or write to file
    if output_file:
        with open(output_file, 'w') as file:
            file.write('\n'.join(output))
        print(f"Folder structure written to {output_file}")
    else:
        print('\n'.join(output))

# Example usage
if __name__ == "__main__":
    list_folder_structure('../../sample_data/2025-08-14-stoic-backup/', '../../sample_data/2025-08-14-stoic-backup/folder_structure.txt')
