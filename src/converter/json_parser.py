import json
import os

def load_json_files(directory: str):
    """Load all JSON files from the specified directory."""
    json_data = {}
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(os.path.join(directory, filename), 'r') as f:
                json_data[filename] = json.load(f)
    return json_data

def process_journal_entries(data):
    """Process journal entries from the loaded JSON data."""
    journal_entries = []
    if 'journal-entries.json' in data:
        entries = data['journal-entries.json']
        for entry in entries:
            # Extract relevant fields and format as needed for Apple Journal
            journal_entry = {
                'date': entry.get('date'),
                'content': entry.get('content'),
                'mood': entry.get('mood'),
                'tags': entry.get('tags', [])
            }
            journal_entries.append(journal_entry)
    return journal_entries

# Example usage
if __name__ == "__main__":
    directory = '../../sample_data/2025-08-14-stoic-backup/'
    json_data = load_json_files(directory)
    journal_entries = process_journal_entries(json_data)
    
    # Print or save the processed journal entries
    for entry in journal_entries:
        print(entry)
