import xlrd


def worker():
    rb = xlrd.open_workbook('excel.xlsx')
    sheet = rb.sheet_by_index(0)
    return sheet