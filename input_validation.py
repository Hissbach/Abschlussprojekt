import os

def validate_file_path(file_path):
    """
    Validates if the given file path exists.

    Parameters:
        - file_path (str): the path to the file to validate

    Returns:
        - bool: True if the file exists, False otherwise
    """
    if not os.path.isfile(file_path):
        print(f"The file '{file_path}' does not exist.")
        return False
    return True


def validate_folder_path(folder_path):
    """
    Validates if the given folder path exists.

    Parameters:
        - folder_path (str): the path to the folder to validate

    Returns:
        - bool: True if the folder exists, False otherwise
    """
    if not os.path.isdir(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return False
    return True
