import pandas as pd

from config import DIRECTORY_PATH, OUTPUT_CSV_PATH
from utils.excel_operations import read_excel_files
from utils.file_operations import get_all_excel_files

import csv


def main():
    excel_files = get_all_excel_files(DIRECTORY_PATH)

    if not excel_files:
        print(f"No se encontraron archivos Excel en el directorio {DIRECTORY_PATH}")
        return

    print(f"Archivos excel encontrados {excel_files}")

    all_data = pd.DataFrame()

    for file_path in excel_files:
        print(f"Leyendo archivo: {file_path}")
        first_file = True

        for df in read_excel_files(file_path, skiprows=2, has_headers=not first_file):
            if first_file:
                all_data = df
                first_file = False
            else:
                all_data.append(df[3:])

    if all_data:
        data = pd.concat(all_data, ignore_index=True)
        data.to_csv(OUTPUT_CSV_PATH, index=False, quoting=csv.QUOTE_MINIMAL, quotechar="'")
        print(f"Datos guardados en la ruta {OUTPUT_CSV_PATH}")
    else:
        print("No se han leído datos de los archivos Excel")


if __name__ == "__main__":
    main()
