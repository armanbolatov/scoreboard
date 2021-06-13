import openpyxl as xl

def dictify(fname, lname, STRUCTURE):
    '''
    Inputs: nothing
    Outputs: a python dictionary mapping college names to various requirements
    '''
    # Let's make a dictionary of all colleges
    DATA = {}
    DB = xl.load_workbook(fname)
    DS = DB[lname]
    i = 2
    while True:
        key = 'A' + str(i)
        if DS[key].value is None:
            break
        internalData = {}
        DATA[DS[key].value] = internalData
        for keyLtr, code in STRUCTURE.items():
            key = keyLtr + str(i)
            internalData[code] = DS[key].value
        i+=1

    return DATA
