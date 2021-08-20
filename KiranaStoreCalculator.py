# from openpyxl import Workbook
# client_database = Workbook()
# wb = client_database.active()
def spreadsheet_writer():
    """This functions checks the row and column by itself and writed the data."""
    with open("data_randc.txt", "r") as f:
        dat = f.read()    
        print(type(dat))    
i = 0
while True:
    v = input()
    if v.lower() == "q":
        print(i)
        break 
    else:
        v = int(v)
        i = i + v
spreadsheet_writer()