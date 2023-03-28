import pandas as pd
import os
import json
import re


FILE_PATH = '/Users/olehissbach/Desktop/Abschlussprojekt/Data/Mappe1.xlsx'
SHEET_NAME = 'Datatabelle'
FOLDER_PATH = '/Users/olehissbach/Desktop/Abschlussprojekt/'
DEFAULT_KEYWORDS = ['martin', 'ole']


def read_excel_to_list(file_path, sheet_name):
    """
    Reads values from an Excel sheet and returns them as a list of strings.

    Parameters:
        - file_path (str): the path to the Excel file
        - sheet_name (str): the name of the sheet to read

    Returns:
        - list: a list of strings representing the values in the sheet
    """
    try:
        # Load the Excel sheet into a pandas DataFrame
        excel_data = pd.read_excel(file_path, sheet_name=sheet_name)
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
        return []
    except PermissionError:
        print(f"You don't have permission to open the file '{file_path}'.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file '{file_path}': {str(e)}")
        return []

    # Convert the DataFrame to a list of strings
    value_list = [val for val in excel_data.values.flatten()]

    return value_list


def search_keywords_in_folder(folder_path, default_keywords, value_list):
    """
    Searches through all the txt files in a folder for keywords using regex.

    Parameters:
        - folder_path (str): the path to the folder containing the txt files
        - default_keywords (list): a list of strings representing the default keywords to search for
        - value_list (list): a list of strings representing additional keywords to search for

    Returns:
        - dict: a dictionary where the keys are the file names and the values are lists of the keywords found in each file
    """
    # Combine the default keywords and value_list
    all_keywords = set(default_keywords + value_list)

    results = {}
    error_files = []

    # Check if folder_path is valid
    if not os.path.isdir(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return results

    # Loop through each file in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)

            # Read the file and search for the keywords using regex
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    contents = f.read().lower()
                    file_keywords = [keyword.lower() for keyword in all_keywords if re.search(r'\b{}\b'.format(keyword.lower()), contents)]
            except UnicodeDecodeError:
                error_files.append(file_name)
                continue

            # Add the results to the dictionary
            if file_keywords:
                results[file_name] = file_keywords

    # Export the results to a json file
    with open('results.json', 'w') as f:
        json.dump(results, f, indent=4)

    # Print the error files, if any
    if error_files:
        print("The following files could not be decoded:")
        for error_file in error_files:
            print(f"- {error_file}")

    return results


values = read_excel_to_list(FILE_PATH, SHEET_NAME)
results = search_keywords_in_folder(FOLDER_PATH, DEFAULT_KEYWORDS, values)
print(results)
