import os
import unittest
from input_validation import validate_file_path, validate_folder_path

class TestInputValidation(unittest.TestCase):
    def test_validate_file_path_exists(self):
        # create a test file
        test_file_path = "test_file.txt"
        open(test_file_path, "w").close()

        result = validate_file_path(test_file_path)
        self.assertTrue(result)

        # delete the test file
        os.remove(test_file_path)

    def test_validate_file_path_does_not_exist(self):
        result = validate_file_path("non_existent_file.txt")
        self.assertFalse(result)

    def test_validate_folder_path_exists(self):
        # create a test folder
        test_folder_path = "test_folder"
        os.makedirs(test_folder_path, exist_ok=True)

        result = validate_folder_path(test_folder_path)
        self.assertTrue(result)

        # delete the test folder
        os.rmdir(test_folder_path)

    def test_validate_folder_path_does_not_exist(self):
        result = validate_folder_path("non_existent_folder")
        self.assertFalse(result)
