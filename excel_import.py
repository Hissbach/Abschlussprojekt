import pandas as pd


def read_excel_to_list(file_path: str, sheet_name: str) -> list:
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

    # Convert the DataFrame to a list of strings
    value_list = [val for val in excel_data.values.flatten() if str(val) != 'nan']

    return value_list
