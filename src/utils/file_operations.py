import os
import glob


def get_all_excel_files(directory):
    excel_files = glob.glob(os.path.join(directory, "**", "*.xls*"), recursive=True)
    return excel_files
