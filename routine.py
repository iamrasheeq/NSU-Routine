# import tabulate  library
# pip install tabulate

import webbrowser
import os
from tabulate import tabulate

course = [
    ["MAT250", "ST", '4:20 - 5:50'],
    ["BEN205", "RA", '4:20 - 5:50'],
    ["BIO103", "MW", '2:40 - 4:10'],
    ["PHI104", "ST", '9:40 - 11:10'],
    ["HIS102", "MW", '9:40 - 11:10']
]

table = [["NSU", '8:00 - 9:40', '9:40 - 11:10', '11:20 - 12:50', '1:00 - 2:30', '2:40 - 4:10', '4:20 - 5:50'],
         ["SAT", '8:00 - 9:40', '9:40 - 11:10', '11:20 - 12:50', '1:00 - 2:30', '2:40 - 4:10', '4:20 - 5:50'],
         ["SUN", '8:00 - 9:40', '9:40 - 11:10', '11:20 - 12:50', '1:00 - 2:30', '2:40 - 4:10', '4:20 - 5:50'],
         ["MON", '8:00 - 9:40', '9:40 - 11:10', '11:20 - 12:50', '1:00 - 2:30', '2:40 - 4:10', '4:20 - 5:50'],
         ["TUE", '8:00 - 9:40', '9:40 - 11:10', '11:20 - 12:50', '1:00 - 2:30', '2:40 - 4:10', '4:20 - 5:50'],
         ["WED", '8:00 - 9:40', '9:40 - 11:10', '11:20 - 12:50', '1:00 - 2:30', '2:40 - 4:10', '4:20 - 5:50'],
         ["THU", '8:00 - 9:40', '9:40 - 11:10', '11:20 - 12:50', '1:00 - 2:30', '2:40 - 4:10', '4:20 - 5:50'],
         ]
blank = "__"

for k in range(0, len(course)):
    if course[k][1] == "ST":
        c = 0
        for i in table[2]:
            if course[k][2] == i:
                table[2][c] = course[k][0]
            c += 1
        c = 0
        for i in table[4]:
            if course[k][2] == i:
                table[4][c] = course[k][0]
            c += 1
    elif course[k][1] == "MW":
        c = 0
        for i in table[3]:
            if course[k][2] == i:
                table[3][c] = course[k][0]
            c += 1
        c = 0
        for i in table[5]:
            if course[k][2] == i:
                table[5][c] = course[k][0]
            c += 1
    elif course[k][1] == "RA":
        c = 0
        for i in table[1]:
            if course[k][2] == i:
                table[1][c] = course[k][0]
            c += 1
        c = 0
        for i in table[6]:
            if course[k][2] == i:
                table[6][c] = course[k][0]
            c += 1

for i in range(1, 7):
    c = 0
    for j in table[i]:
        if j[0].isnumeric():
            table[i][c] = blank
        c += 1


# print(tabulate(table))

with open("web/header.html") as f:
    with open("web/index.html", "w") as fileMain:
        for line in f:
            fileMain.write(line)
        with open("web/body.html", mode="w") as ff:
            print(tabulate(table, tablefmt='html'), file=ff)

        with open("web/body.html") as ff:
            newText = ff.read().replace('<table>', '<table class="table table-bordered table-striped">')
        with open("web/body.html", "w") as ff:
            ff.write(newText)
        with open("web/body.html") as ff:
            for line in ff:
                fileMain.write(line)

        with open("web/footer.html") as f1:
            for line in f1:
                fileMain.write(line)
                
print("successful")
ff.close()
f1.close()
fileMain.close()
f.close()

webbrowser.open('file://' + os.path.realpath('web/index.html'))

# with open("body.html", mode="w") as writeFile:
#     print(tabulate(table, tablefmt='html'), file=writeFile)
#     writeFile.close()
