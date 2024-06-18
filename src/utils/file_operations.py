import os
import pandas as pd
import csv
from src.config import OUTPUT_CSV_PATH
from src.utils.excel_operations import process_excel_file


def get_all_excel_files(directory):
    all_data = pd.DataFrame()

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".xlsx"):
                file_path = os.path.join(root, file)
                print(f"Leyendo archivo {file_path}")
                file_data = process_excel_file(file_path)
                all_data = pd.concat([all_data, file_data], ignore_index=True)

    return all_data


def save_csv(data):
    data.to_csv(OUTPUT_CSV_PATH, index=False, quoting=csv.QUOTE_MINIMAL, quotechar="'")

