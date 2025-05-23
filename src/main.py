import argparse
from converter.parser import JournalParser
from converter.formatter import MarkdownFormatter
from utils.file_handler import FileHandler
from utils.folder_manager import FolderManager

def main():
    parser = argparse.ArgumentParser(description='Convert Stoic journal entries to Obsidian notes')
    parser.add_argument('input_file', help='Input JSON file containing Stoic journal entries')
    parser.add_argument('output_dir', help='Output directory for Obsidian notes')
    parser.add_argument('--clean', action='store_true', help='Clean output directory before conversion')
    
    args = parser.parse_args()

    # Initialize components
    folder_manager = FolderManager(args.output_dir)
    file_handler = FileHandler(args.output_dir)
    journal_parser = JournalParser(args.input_file)
    
    # Create folder structure
    if args.clean:
        folder_manager.clean_folders()
    else:
        folder_manager.create_folder_structure()
    
    # Parse and convert entries
    entries = journal_parser.parse()
    
    # Process each entry
    for entry in entries:
        note = MarkdownFormatter.format_entry(entry)
        file_handler.save_note(note)
        
    print(f"Successfully converted {len(entries)} entries to Obsidian notes")

if __name__ == "__main__":
    main()