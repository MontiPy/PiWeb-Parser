import extract
import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog
import sys


def convert_name_2_excel(file_path):
    base_name = os.path.basename(file_path).split('.')[0]
    download_path = os.path.join(os.getenv('USERPROFILE'), 'Downloads')
    excel_path = os.path.join(download_path, base_name + '.xlsx')
    return excel_path


def run_CMM():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title='Select CSV File', filetypes=[('CSV', '.csv')])

    cmm_excel_path = convert_name_2_excel(file_path)
    df = pd.read_csv(file_path)

    with pd.ExcelWriter(cmm_excel_path) as writer:
        extract.extract_CMM(df).to_excel(writer, sheet_name=os.path.basename(
            cmm_excel_path).split('.')[0], index=False)

    print(f'CMM DATA STORED AT: {cmm_excel_path}')


while __name__ == "__main__":
    answer = input("Do you want to process PiWeb CMM Data? (Y/N): ").upper()
    if answer == "Y":
        run_CMM()
    elif answer == "N":
        sys.exit()
    else:
        print("Please enter 'Y' or 'N' for answer.")
    
