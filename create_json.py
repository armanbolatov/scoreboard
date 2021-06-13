import openpyxl as xl
import parse
import codes_oblasts
import codes_countries
import json
import structures

# icho = {'icho.xlsx': ["2010"]}

# formats raw .xlsx data into format that can be read by the function jsonify()
def codify(dic, rounds, international):
    ''' inputs rawDic '''
    coded = []
    for _, _data in dic.items():
        summary = {'nameEn': _data['nameEn'], 'nameKk': _data['nameKk'], 'nameRu': _data['nameRu']}
        val = _data['medal']
        if val is None or "":
            summary['medal'] = 'none'
        else:
            summary['medal'] = val
        obl = _data['oblast']
        if obl in codes_oblasts.oblToCode:
            summary['school'] = codes_oblasts.oblToCode[obl]
        else:
            summary['school'] = 20
        if international:
            country = _data['country']
            if country in codes_countries.countryToCode:
                summary['country'] = codes_countries.countryToCode[country]
            else:
                summary['country'] = 'XX'
        vals = []
        for i in range(1, rounds+1):
            buildKey = 'round' + str(i)
            vals.append(_data[buildKey])
        summary['rounds'] = vals
        coded.append(summary)
    return coded

# creates .json file for upload to scoreboard.kz
def jsonify(fcodes, year, rounds, structure, international):
    for _fname, shnames in fcodes.items():
        fname = 'source/'+str(year)+'/' + _fname
        for shname in shnames:
            dic = parse.dictify(fname, shname, structure)
            newL = codify(dic, rounds, international)
            with open('output/'+str(year)+'/'+_fname[:-5]+shname+'.json', 'w', encoding='utf8') as json_file:
                json.dump(newL, json_file, ensure_ascii=False, indent=2)

# jsonify(icho, 'icho', 2, structures.STRUC_ISO, True)
