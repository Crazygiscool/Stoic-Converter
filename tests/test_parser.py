import unittest
from src.converter.parser import Parser

class TestParser(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()

    def test_parse_valid_entry(self):
        entry = "2023-10-01: Today I learned about stoicism."
        parsed_entry = self.parser.parse(entry)
        self.assertEqual(parsed_entry.title, "2023-10-01")
        self.assertEqual(parsed_entry.content, "Today I learned about stoicism.")

    def test_parse_invalid_entry(self):
        entry = "Invalid entry format"
        with self.assertRaises(ValueError):
            self.parser.parse(entry)

    def test_parse_multiple_entries(self):
        entries = [
            "2023-10-01: First entry.",
            "2023-10-02: Second entry."
        ]
        parsed_entries = self.parser.parse_multiple(entries)
        self.assertEqual(len(parsed_entries), 2)
        self.assertEqual(parsed_entries[0].title, "2023-10-01")
        self.assertEqual(parsed_entries[1].title, "2023-10-02")

if __name__ == '__main__':
    unittest.main()