import csv

eSet = set()

url = "../../data/NewRawData/version.csv"


# 创建和写文件函数
def create_csv():
    path = url
    with open(path, 'w') as f:
        csv_write = csv.writer(f)


def write_csv(c):
    path = url
    with open(path, 'a+', newline='', encoding='utf-8') as f:
        csv_write = csv.writer(f)
        data_row = c
        csv_write.writerow(data_row)


# eFile = open("../../data/raw/errorMovie.csv", "r", encoding="utf-8")
# eRedaer = csv.reader(eFile)
# for item in eRedaer:
#     eSet.add(item[0][89:99])

# eDict = {}
# mFile = open("../../data/MergedData/mergedData.csv", "r", encoding="utf-8")
# mReader = csv.reader(mFile)
# for item in mReader:
#     if item[0] in eSet and item[4] != "":
#         eDict[item[0]] = item[4]
if __name__ == "__main__":
    create_csv()
    # firstLine = "id", "title", "director", "actors", "year", "month", "day", "weekday", "version", "tag", "rate", "reviewNum", "five", "four", "three", "two", "one"
    # write_csv(firstLine)
    csvfile = open("../../data/NewRawData/last.csv", "r", encoding="utf-8")
    reader = csv.reader(csvfile)
    i = 0
    vset = set()
    for line in reader:
        vset.add(line[8])
    create_csv()
    for item in vset:
        content = item,
        write_csv(content)
