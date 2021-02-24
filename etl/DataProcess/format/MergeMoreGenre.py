import csv

# eSet = set()
#
# eFile = open("../../../data/raw/errorMovie.csv", "r", encoding="utf-8")
# eRedaer = csv.reader(eFile)
# for item in eRedaer:
#     eSet.add(item[0][89:99])
#
# eDict = {}
# mFile = open("../../../data/MergedData/mergedData.csv", "r", encoding="utf-8")
# mReader = csv.reader(mFile)
# for item in mReader:
#     if item[0] in eSet and item[4] != "":
#         eDict[item[0]] = item[4]
#
# nfdFile = open("../../../data/NewRawData/NameFormatData.csv", "r", encoding="utf-8")
# nfdReader = csv.reader(nfdFile)
# for line in nfdFile:
#     print(line)

enfdFile = open("../../../data/NewRawData/GenreNameFormatData.csv", "r", encoding="utf-8")
enfdReader = csv.reader(enfdFile)
for line in enfdReader:
    print(line[9])
