letters = {
    "ә": "а",
    "Ә": "А",
    "і": "и",
    "І": "И",
    "ң": "н",
    "Ң": "Н",
    "ғ": "г",
    "Ғ": "Г",
    "ү": "у",
    "Ү": "У",
    "ұ": "у",
    "Ұ": "У",
    "қ": "к",
    "Қ": "К",
    "һ": "х",
    "Һ": "Х",
    "ө": "о",
    "Ө": "О",
}

with open('k2r.txt', encoding = 'utf-8', mode = 'r') as f:
    lines = f.readlines()

fp = open("k2r_parsed.txt", encoding = 'utf-8', mode = 'a')
for line in lines:
    newline = ""
    for s in line:
        if s in letters: s = letters[s]
        newline += s
    fp.write(newline)
fp.close()
