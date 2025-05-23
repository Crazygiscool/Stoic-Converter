import unittest
from src.converter.formatter import Formatter

class TestFormatter(unittest.TestCase):

    def setUp(self):
        self.formatter = Formatter()

    def test_format_entry(self):
        entry = {
            'title': 'My First Journal Entry',
            'content': 'Today I learned about Stoicism.',
            'date': '2023-10-01'
        }
        expected_output = "# My First Journal Entry\n\nToday I learned about Stoicism.\n\n---\n\n"
        formatted_entry = self.formatter.format_entry(entry)
        self.assertEqual(formatted_entry, expected_output)

    def test_format_multiple_entries(self):
        entries = [
            {
                'title': 'Entry 1',
                'content': 'Content for entry 1.',
                'date': '2023-10-01'
            },
            {
                'title': 'Entry 2',
                'content': 'Content for entry 2.',
                'date': '2023-10-02'
            }
        ]
        expected_output = "# Entry 1\n\nContent for entry 1.\n\n---\n\n# Entry 2\n\nContent for entry 2.\n\n---\n\n"
        formatted_entries = self.formatter.format_multiple_entries(entries)
        self.assertEqual(formatted_entries, expected_output)

if __name__ == '__main__':
    unittest.main()