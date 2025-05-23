import unittest
from src.utils.file_handler import read_file, write_file

class TestFileHandler(unittest.TestCase):

    def test_read_file(self):
        # Test reading a file
        content = read_file('sample_data/test_journal.txt')
        self.assertIsInstance(content, str)
        self.assertGreater(len(content), 0)

    def test_write_file(self):
        # Test writing to a file
        test_content = "This is a test journal entry."
        write_file('sample_data/test_output.txt', test_content)
        with open('sample_data/test_output.txt', 'r') as f:
            content = f.read()
        self.assertEqual(content, test_content)

    def test_write_empty_file(self):
        # Test writing an empty file
        write_file('sample_data/test_empty_output.txt', '')
        with open('sample_data/test_empty_output.txt', 'r') as f:
            content = f.read()
        self.assertEqual(content, '')

if __name__ == '__main__':
    unittest.main()