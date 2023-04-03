import pandas as pd


def read_excel_to_dict(file_path: str, sheet_name: str) -> dict:
    """
    Liest Werte aus einer Excel-Datei und gibt sie als Dictionary aus

    Parameters:
        - file_path (str): Pfad zur Excel-Datei
        - sheet_name (str): Name der Tabelle (muss vllt noch rausgenommen werden könnte Probleme bereiten)

    Returns:
        - dict: Ein Dictionary, mit den Werten aus der Excel Datei, wobei die Spaltennamen als Schlüssel verwendet werden.
    """
    try:
        # Load the Excel sheet into a pandas DataFrame
        excel_data = pd.read_excel(file_path, sheet_name)
        # Check if the sheet is empty
        if excel_data.empty:
            print(f"The sheet '{sheet_name}' in '{file_path}' is empty.")
            return {}
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
        return {}
    except PermissionError:
        print(f"You don't have permission to open the file '{file_path}'.")
        return {}
    except Exception as e:
        print(f"An error occurred while reading the file '{file_path}': {str(e)}")
        return {}

    # Convert the DataFrame to a dictionary using the first row as keys
    excel_dict = excel_data.to_dict(orient='list')
    # Remove any NaN values from the dictionary
    excel_dict = {k: [x for x in v if str(x) != 'nan'] for k, v in excel_dict.items()}
    print(excel_dict)
    return excel_dict
