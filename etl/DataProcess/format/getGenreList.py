import csv

url = "../../../data/raw/genreList.csv"


def create_csv():
    path = url
    with open(path, 'w') as f:
        csv_write = csv.writer(f)


def write_csv(content):
    path = url
    with open(path, 'a+', newline='', encoding='utf-8') as f:
        csv_write = csv.writer(f)
        data_row = content
        csv_write.writerow(data_row)


eSet = set()

eFile = open("../../../data/raw/errorMovie.csv", "r", encoding="utf-8")
eRedaer = csv.reader(eFile)
for item in eRedaer:
    eSet.add(item[0][89:99])

eDict = {}
mFile = open("../../../data/MergedData/mergedData.csv", "r", encoding="utf-8")
mReader = csv.reader(mFile)
for item in mReader:
    if item[0] in eSet and item[4] != "":
        eDict[item[0]] = item[4]

genreSet = set()

for item in eDict:
    temp = eDict[item].split(",")
    for iitem in temp:
        ttemp = iitem.split("and")
        for iiiitem in ttemp:
            genreSet.add(iiiitem.strip().lower())

create_csv()
for item in genreSet:
    content = item,
    write_csv(content)

# nfdFile = open("../../../data/NewRawData/NameFormatData.csv", "r", encoding="utf-8")
# nfdReader = csv.reader(nfdFile)
# for line in nfdFile:
#     print(line)

# enfdFile = open("../../../data/NewRawData/GenreNameFormatData.csv", "r", encoding="utf-8")
# enfdReader = csv.reader(enfdFile)
# for line in enfdReader:
#     print(line[9])
