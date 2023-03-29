import os
import json
import re
from typing import List, Dict


def search_keywords_in_folder(folder_path: str, default_keywords: List[str], value_list: List[str]) -> Dict[str, List[str]]:
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
    all_keywords = default_keywords + value_list

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
