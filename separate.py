import openpyxl as xl

def stringify(l):
    start = ''
    for item in l:
        start += item
        start += ','
    return start[:-1]

for fname in fnames:
    WB = xl.load_workbook('source/2017/' + fname + '.xlsx')
    for sheet in WB:
        i = 2
        while True:
            cell = sheet['H' + str(i)]
            if cell.value is None:
                break
            array = cell.value.split(',')
            sheet['H' + str(i)] = array[0]
            sheet['I' + str(i)] = stringify(array[1:])
            i+=1
    WB.save('source/2017/' + fname + '.xlsx')
