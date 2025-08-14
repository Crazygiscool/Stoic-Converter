from converter.json_parser import load_json_files, process_journal_entries

def main():
    # Specify the directory containing the JSON files
    json_directory = '../../sample_data/2025-08-14-stoic-backup/'
    
    # Load JSON files
    json_data = load_json_files(json_directory)
    
    # Process journal entries
    journal_entries = process_journal_entries(json_data)
    
    # Further processing or conversion logic here
    for entry in journal_entries:
        print(entry)

if __name__ == "__main__":
    main()
