import pandas as pd


def read_excel_to_list(file_path: str, sheet_name: str) -> list:
    """
    Liest Werte aus einer Excel-Datei und gibt sie als Liste an Strings aus

    Parameters:
        - file_path (str): Pfad zur Excel-Datei
        - sheet_name (str): Name der Tabelle (muss vllt noch rausgenommen werden könnte Probleme bereiten)

    Returns:
        - list: Eine Liste an Strings, mit den Werten aus der Excel Datei
    """
    try:
        # Load the Excel sheet into a pandas DataFrame
        excel_data = pd.read_excel(file_path, sheet_name)
        # Check if the sheet is empty
        if excel_data.empty:
            print(f"The sheet '{sheet_name}' in '{file_path}' is empty.")
            return []
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
        return []
    except PermissionError:
        print(f"You don't have permission to open the file '{file_path}'.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file '{file_path}': {str(e)}")
        return []
    

    # Convert all values in the DataFrame to strings
    excel_data = excel_data.astype(str)
    # Convert the DataFrame to a list of strings
    value_list = [val for val in excel_data.values.flatten() if str(val) != 'nan']
    print(value_list)
    return value_list
