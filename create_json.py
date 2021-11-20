import openpyxl as xl
import parse
import codes_oblasts as co
import codes_countries as cc
import json
import structures

# izho_cs = {'izho_cs.xlsx': ['2021', '2020']}

def codify(dic, rounds, international):
    coded = []
    for _, _data in dic.items():
        summary =  {'nameEn': _data['nameEn'],
                    'nameKk': _data['nameKk'],
                    'nameRu': _data['nameRu']}
        val = _data['medal']
        summary['medal'] = 'none' if val is None or "" else val
        obl = _data['oblast']
        summary['school'] = co.oblToCode[obl] if obl in \
                            co.oblToCode else 20
        if international:
            country = _data['country']
            summary['country'] = cc.countryToCode[country] if country in \
                                 cc.countryToCode else 'XX'
        vals = []
        for i in range(1, rounds+1):
            buildKey = 'round' + str(i)
            vals.append(_data[buildKey])
        summary['rounds'] = vals
        coded.append(summary)
    return coded

def jsonify(fcodes, year, rounds, structure, international):
    for _fname, shnames in fcodes.items():
        fname = 'source/'+str(year)+'/' + _fname
        for shname in shnames:
            dic = parse.dictify(fname, shname, structure)
            newL = codify(dic, rounds, international)
            with open('output/' + str(year) + '/' + _fname[:-5] + shname + '.json',
                      'w', encoding='utf8') as json_file:
                json.dump(newL, json_file, ensure_ascii=False, indent=2)

# jsonify(izho_cs, 'izho_cs', 2, structures.STRUC_ISO, True)
