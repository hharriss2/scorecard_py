from os import listdir
import os
from os.path import isfile, join
import openpyxl as xl
onlyfiles = [f for f in listdir(
    "/Users/harris-jones/Documents/coding2021/exceltest/") if isfile(join("/Users/harris-jones/Documents/coding2021/exceltest/", f))]

excel_files = onlyfiles

print(excel_files[1])

filename = "/Users/harris-jones/Documents/coding2021/exceltest/"+excel_files[1]

wb1 = xl.load_workbook(filename)
ws1 = wb1.worksheets[0]

get_file_name = ws1.cell(row=1, column=2)

new_file_name = get_file_name.value
os.rename(filename, new_file_name,)
