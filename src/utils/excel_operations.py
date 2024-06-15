import re

import pandas as pd
from utils.data_operations import rename_columns_to_snake_case
from openpyxl import load_workbook


def to_snake_case(name):
    """Convert CamelCase to snake_case."""
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def read_excel_files(file_path, skiprows, has_headers):
    xls = pd.ExcelFile(file_path)
    all_dfs = []

    for sheet_name in xls.sheet_names:
        print(f"Reading sheet: {sheet_name} from file: {file_path}")
        df = pd.read_excel(xls, sheet_name=sheet_name, skiprows=skiprows)
        df = rename_columns_to_snake_case(df)

        if df.isnull().all(axis=1).any():
            empty_row_index = df.isnull().all(axis=1).idxmax()

            df = df.iloc[:empty_row_index]

        df = fill_merged_rows(file_path, sheet_name, df)
        if not has_headers:
            all_dfs.append(df)
        else:
            all_dfs.append(df[1:])

    return pd.concat(all_dfs, ignore_index=True)


def fill_merged_rows(file_path, sheet_name, df):
    workbook = load_workbook(file_path, data_only=True)
    sheet = workbook[sheet_name]

    for merged_sheet_cell in sheet.merged_cells.ranges:
        min_col, min_row, max_col, max_row = merged_sheet_cell.bounds
        merged_value = sheet.cell(row=min_row, column=min_col)
        merged_value = str(merged_value)

        for row in range(min_row, max_row + 1):
            for col in range(min_col, max_col + 1):
                if row - 1 < df.shape[0] and col - 1 < df.shape[1]:
                    current_value = df.iloc[row - 1, col - 1]

                    # Convert merged_value to a compatible dtype if needed
                    if isinstance(current_value, str):
                        merged_value = str(merged_value)
                    elif isinstance(current_value, int):
                        try:
                            merged_value = int(merged_value)
                        except (ValueError, TypeError):
                            # Handle cases where merged_value cannot be converted to int
                            merged_value = None  # or any other appropriate handling

                    # Assign merged_value to the DataFrame cell
                    if merged_value is not None:
                        df.iloc[row - 1, col - 1] = merged_value


    return df


