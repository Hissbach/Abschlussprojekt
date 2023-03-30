import os

def validate_file_path(file_path):
    """
    Validiert das der Filepath korrekt ist

    Parameters:
        - file_path (str): der Pfad zur Datei

    Returns:
        - bool: True wenn Datei existiert, False wenn nicht
    """
    if not os.path.isfile(file_path):
        print(f"The file '{file_path}' does not exist.")
        return False
    return True


def validate_folder_path(folder_path):
    """
    Validiert ob ein Dateiordner existiert

    Parameters:
        - folder_path (str): Der Pfad zum Ordner

    Returns:
        - bool: True wenn Ordner existiert; sonst False
    """
    if not os.path.isdir(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return False
    return True
