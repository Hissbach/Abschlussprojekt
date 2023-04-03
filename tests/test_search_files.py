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
        
    def test_search_keywords_in_folder_no_files(self):
        expected_results = {}
        value_list = ['keyword1', 'keyword2']
        test_folder = tempfile.mkdtemp()
        results = search_keywords_in_folder(test_folder, value_list)
        self.assertDictEqual(results, expected_results)
        shutil.rmtree(test_folder)
        
    def test_search_keywords_in_folder_no_keywords(self):
        expected_results = {'test1.txt': [], 'test2.txt': []}
        value_list = []
        test_folder = tempfile.mkdtemp()
        test_files = ['test1.txt', 'test2.txt']
        for test_file in test_files:
            with open(os.path.join(test_folder, test_file), 'w', encoding='utf-8') as f:
                f.write(f'This is a test file for {test_file}. It contains no keywords.')
        results = search_keywords_in_folder(test_folder, value_list)
        self.assertDictEqual(results, expected_results)
        shutil.rmtree(test_folder)
        
    def test_search_keywords_in_folder_encoding_error(self):
        expected_results = {}
        value_list = ['keyword1', 'keyword2']
        test_folder = tempfile.mkdtemp()
        test_file = 'test1.txt'
        with open(os.path.join(test_folder, test_file), 'wb') as f:
            f.write(b'\x80\x81\x82')
        results = search_keywords_in_folder(test_folder, value_list)
        self.assertDictEqual(results, expected_results)
        shutil.rmtree(test_folder)
        
      
    def tearDown(self):
        shutil.rmtree(self.test_folder)
