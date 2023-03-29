import unittest
import pandas as pd
from unittest.mock import patch
from excel_import import read_excel_to_list

class TestReadExcelToList(unittest.TestCase):
    @patch('pandas.read_excel')
    def test_read_excel_file_not_found(self, mock_read_excel):
        mock_read_excel.side_effect = FileNotFoundError
        result = read_excel_to_list('fake_file.xlsx', 'Sheet1')
        self.assertEqual(result, [])
    @patch('pandas.read_excel')
    def test_read_excel_permission_error(self, mock_read_excel):
        mock_read_excel.side_effect = PermissionError
        result = read_excel_to_list('fake_file.xlsx', 'Sheet1')
        self.assertEqual(result, [])
    @patch('pandas.read_excel')
    def test_read_excel_empty_sheet(self, mock_read_excel):
        mock_read_excel.return_value = pd.DataFrame()
        result = read_excel_to_list('file.xlsx', 'Sheet1')
        self.assertEqual(result, [])
    
    @patch('pandas.read_excel')
    def test_read_excel_general_error(self, mock_read_excel):
        mock_read_excel.side_effect = ValueError('Mock error')
        result = read_excel_to_list('file.xlsx', 'Sheet1')
        self.assertEqual(result, [])
    @patch('pandas.read_excel')
    def test_read_excel_success(self, mock_read_excel):
        mock_data = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        mock_read_excel.return_value = mock_data
        result = read_excel_to_list('file.xlsx', 'Sheet1')
        self.assertEqual(result, [1, 3, 2, 4])