import excel_import
import search_files

FILE_PATH = '/Users/olehissbach/Desktop/Abschlussprojekt/Data/Mappe1.xlsx'
SHEET_NAME = 'Datatabelle'
FOLDER_PATH = '/Users/olehissbach/Desktop/Abschlussprojekt/'
DEFAULT_KEYWORDS = ['martin', 'ole']

values = excel_import.read_excel_to_list(FILE_PATH, SHEET_NAME)
results = search_files.search_keywords_in_folder(FOLDER_PATH, DEFAULT_KEYWORDS, values)
print(results)
