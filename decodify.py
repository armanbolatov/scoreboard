import openpyxl as xl
import codes_oblasts

# fname = 'source/2019/biology.xlsx'
# shnames = ['9 grade', '10 grade', '11 grade']

# converts .xlsx file into readable format
WB = xl.load_workbook(fname)
for shname in shnames:
    WS = WB[shname]
    i = 2
    while True:
        cell = WS['H'+str(i)]
        if cell.value is None:
            break
        key = cell.value
        if type(key) == int:
            WS['H'+str(i)] = codes_oblasts.codeToOblast[key]
        i+=1

# WB.save('source/2019/biology_new.xlsx')
