import os
from openpyxl import load_workbook

path = "./files"
file_list = os.listdir(path)
print(file_list)

results = []
for file_name_raw in file_list:
    file_name = "./files/" + file_name_raw
    wb = load_workbook(filename = file_name, data_only=True)
    ws = wb.active