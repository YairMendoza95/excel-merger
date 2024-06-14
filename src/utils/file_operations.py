import os


def get_all_excel_files(directory):
    excel_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".xlsx") or file.endswith(".xls"):
                excel_files.append(os.path.join(root, file))

    return excel_files
