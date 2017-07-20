import xlrd, xlwt

rb = xlrd.open_workbook('excel.xlsx')


sheet = rb.sheet_by_index(0)
val = sheet.row_values(24)[6]
print(val)