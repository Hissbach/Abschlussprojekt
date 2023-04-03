import os
import json
import re
from typing import List, Dict


def search_keywords_in_folder(folder_path: str, default_keywords: List[str], value_list: List[str]) -> Dict[str, List[str]]:
    """
    Sucht durch alle .txt Datein in einem Ordner nach Schlüsselworten mit regex

    Parameters:
        - folder_path (str): Pfad zum Ordner mit den txt Datein
        - default_keywords (list): Liste an Standard Schlüsselworten die bei jedem Programmdurchlauf abgefragt werden sollen
        - value_list (list): Liste an Schlüsselworten die zusätzlich noch abgefragt werden sollen (aus der Excel Liste)

    Returns:
        - dict: Ein Dictionary wo die Dateinamen Keys sind mit einer Liste aus gefunden schlüsselworten als Value für jede Datei
    """
    # Kombiniert default_ und excel_Keywords
    all_keywords = default_keywords + value_list

    results = {}
    error_files = {}

    # Loopt durch alle Datein im Zielordner
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)

            # Ließt die Datei und sucht nach Keywords mit Regex
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    contents = f.read().lower()

                    # Sucht nach "Preis in Euro" mit einer optionalen Dezimalstelle
                    match = re.search(r'preis in euro: (\d+(?:\.\d+)?)', contents)
                    if match:
                        price = float(match.group(1))
                        results[file_name] = ['Preis in Euro: {}'.format(price)]
                    else:
                        results[file_name] = []

                    # Sucht nach allen anderen Keywords
                    file_keywords = [keyword.lower() for keyword in all_keywords if re.search(r'\b{}\b'.format(keyword.lower()), contents)]
            except UnicodeDecodeError:
                error_files[file_name] = 'decode_error'
                continue

            # Checkt, ob die Datei alle default Schlüsselwörter enthält
            if not set(default_keywords).issubset(file_keywords):
                error_files[file_name] = 'missing_keywords'
                continue

            # Übergibt Ergebnis ins Dictionary
            if file_keywords:
                results[file_name] += file_keywords

    # Exportiert Ergebnis in einer JSON-Datei
    with open('results.json', 'w') as f:
        json.dump(results, f, indent=4)

    # Exportiert Fehler-Dateien in einer separaten JSON-Datei
    with open('error_files.json', 'w') as f:
        json.dump(error_files, f, indent=4)

    # Gibt Error-Files aus welche nicht gelesen werden konnten oder fehlende Schlüsselwörter haben
    if error_files:
        print("The following files have errors:")
        for error_file, error_type in error_files.items():
            if error_type == 'decode_error':
                print(f"- {error_file}: Decode error")
            elif error_type == 'missing_keywords':
                print(f"- {error_file}: Missing keywords")

    return results
