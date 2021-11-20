import openpyxl as xl
import codes_oblasts

WB = xl.load_workbook(fname)
for shname in shnames:
    WS = WB[shname]
    i = 2
    while True:
        cell = WS['H' + str(i)]
        if cell.value is None:
            break
        key = cell.value
        if type(key) == int:
            WS['H' + str(i)] = codes_oblasts.codeToOblast[key]
        i += 1
