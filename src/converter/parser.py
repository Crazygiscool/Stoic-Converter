import yaml
import zipfile
from datetime import datetime
from typing import List
import os
from ..models.journal_entry import JournalEntry

class JournalParser:
    def __init__(self, zip_file: str):
        self.zip_file = zip_file

    def parse(self) -> List[JournalEntry]:
        """Parse Stoic journal YAML files from zip archive into JournalEntry objects."""
        entries = []
        
        with zipfile.ZipFile(self.zip_file, 'r') as archive:
            # Filter only YAML files
            yaml_files = [f for f in archive.namelist() if f.endswith(('.yaml', '.yml'))]
            
            for yaml_file in yaml_files:
                with archive.open(yaml_file) as f:
                    try:
                        data = yaml.safe_load(f)
                        if data:  # Skip empty files
                            # Extract date from filename or use current date as fallback
                            date_str = os.path.splitext(os.path.basename(yaml_file))[0]
                            try:
                                timestamp = datetime.strptime(date_str, '%Y-%m-%d')
                            except ValueError:
                                timestamp = datetime.now()  # Fallback if no valid date found
                            
                            journal_entry = JournalEntry(
                                timestamp=timestamp,
                                morning_reflection=data.get('morning_reflection'),
                                evening_reflection=data.get('evening_reflection'),
                                gratitude=data.get('gratitude'),
                                quote=data.get('quote'),
                                mood=data.get('mood'),
                                tags=data.get('tags', [])
                            )
                            entries.append(journal_entry)
                    except yaml.YAMLError as e:
                        print(f"Error parsing {yaml_file}: {str(e)}")
                        continue
        
        # Sort entries by date
        entries.sort(key=lambda x: x.timestamp)
        return entries
