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

    for merged_cell_range in sheet.merged_cells.ranges:
        min_col, min_row, max_col, max_row = merged_cell_range.bounds
        merged_value = sheet.cell(row=min_row, column=min_col).value

        for row in range(min_row, max_row + 1):
            for col in range (min_col, max_col + 1):
                df.iat[row - 1, col - 1] = merged_value

    return df