import pandas as pd

from config import DIRECTORY_PATH, OUTPUT_CSV_PATH
from utils.file_operations import get_all_excel_files, save_csv


def main():
    all_data = get_all_excel_files(DIRECTORY_PATH)
    save_csv(all_data)

    print(f"Datos guardados en {OUTPUT_CSV_PATH}")


if __name__ == "__main__":
    main()
