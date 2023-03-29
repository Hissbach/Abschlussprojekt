import unittest
import tempfile
import shutil
import os
from search_files import search_keywords_in_folder

class TestSearchKeywordsInFolder(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory and write some txt files for testing
        self.tempdir = tempfile.mkdtemp()
        file1_path = os.path.join(self.tempdir, 'file1.txt')
        with open(file1_path, 'w') as f:
            f.write('The quick brown fox jumps over the lazy dog.')
        file2_path = os.path.join(self.tempdir, 'file2.txt')
        with open(file2_path, 'w') as f:
            f.write('The lazy dog jumps over the quick brown fox.')
        file3_path = os.path.join(self.tempdir, 'file3.txt')
        with open(file3_path, 'w') as f:
            f.write('This file does not contain any of the keywords.')
        self.files_to_delete = [file1_path, file2_path, file3_path]

    def tearDown(self):
        # Delete the temporary directory and its contents
        shutil.rmtree(self.tempdir)

    def test_search_keywords_in_folder(self):
        # Define the default keywords and additional keywords to search for
        default_keywords = ['quick', 'lazy', 'dog']
        additional_keywords = ['brown', 'fox']

        # Call the function being tested
        result = search_keywords_in_folder(self.tempdir, default_keywords, additional_keywords)

        # Define the expected output
        expected_output = {
            'file1.txt': ['quick', 'lazy', 'dog', 'brown', 'fox'],
            'file2.txt': ['quick', 'lazy', 'dog', 'brown', 'fox']
        }

        # Assert the result is equal to the expected output
        self.assertEqual(result, expected_output)

        # Check if the results file was created
        self.assertTrue(os.path.exists('results.json'))

if __name__ == '__main__':
    unittest.main()
