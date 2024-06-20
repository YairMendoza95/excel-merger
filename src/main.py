import time
import psutil

from config import DIRECTORY_PATH, OUTPUT_CSV_PATH
from utils.file_operations import get_all_excel_files, save_csv


def main():
    start_time = time.time()

    process = psutil.Process()
    initial_memory = process.memory_info().rss / 1024 ** 2

    all_data = get_all_excel_files(DIRECTORY_PATH)
    save_csv(all_data)

    end_time = time.time()

    final_memory = process.memory_info().rss / 1024 ** 2

    print(f"Datos guardados en {OUTPUT_CSV_PATH}")
    print(f"Tiempo de ejecución: {end_time - start_time:.2f} segundos")
    print(f"Uso de memoria: {final_memory - initial_memory:.2f} MB")

if __name__ == "__main__":
    main()
