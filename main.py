from input_validation import validate_file_path, validate_folder_path
import excel_import as excel_import
import search_files as search_files

FILE_PATH = '/Users/olehissbach/Desktop/Abschlussprojekt/Data/Mappe1.xlsx'
SHEET_NAME = 'Datatabelle'
FOLDER_PATH = '/Users/olehissbach/Desktop/Abschlussprojekt/'

if not validate_file_path(FILE_PATH) or not validate_folder_path(FOLDER_PATH):
    exit()

values = excel_import.read_excel_to_list(FILE_PATH, SHEET_NAME)
results = search_files.search_keywords_in_folder(FOLDER_PATH, values)
print(results)
