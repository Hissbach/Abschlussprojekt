import os
import shutil
import tempfile
import unittest
from typing import List, Dict
from search_files import search_keywords_in_folder


class TestSearchKeywordsInFolder(unittest.TestCase):
    
    def setUp(self):
        self.test_folder = tempfile.mkdtemp()
        self.test_files = ['test1.txt', 'test2.txt']
        self.value_list = ['keyword1', 'keyword2']
        for test_file in self.test_files:
            with open(os.path.join(self.test_folder, test_file), 'w', encoding='utf-8') as f:
                f.write(f'This is a test file for {test_file}. It contains {self.value_list[0]} and {self.value_list[1]}.')
        
    def test_search_keywords_in_folder(self):
        expected_results = {
            'test1.txt': ['keyword1', 'keyword2'],
            'test2.txt': ['keyword1', 'keyword2']
        }
        results = search_keywords_in_folder(self.test_folder, self.value_list)
        self.assertDictEqual(results, expected_results)
        
    def tearDown(self):
        shutil.rmtree(self.test_folder)