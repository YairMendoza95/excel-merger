import re

import pandas as pd
from src.utils.data_operations import fill_empty_fields, columns_renamer


def process_excel_file(file_path):
    excel_data = pd.ExcelFile(file_path)
    combined_df = pd.DataFrame()

    for sheet in excel_data.sheet_names:
        df = pd.read_excel(file_path, sheet_name=sheet, usecols="A:AK", skiprows=2)

        print(f"Leyendo hoja {sheet}")
        if df.isnull().all(axis=1).any():
            empty_row = df.isnull().all(axis=1).idxmax()
            df = df.iloc[:empty_row]
        df = fill_empty_fields(df)
        df = columns_renamer(df)

        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df

