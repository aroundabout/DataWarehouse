import csv

url = "../../../data/NewRawData/last.csv"


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


if __name__ == "__main__":
    iadFile = open("../../../data/NewRawData/id_director_actor.csv", "r", encoding="utf-8")
    iadreader = csv.reader(iadFile)
    i = 0
    idwithoutActor = set()
    idActor = {}
    idDirector = {}
    idName = {}

    for item in iadreader:
        temp = item[0].strip().strip("'")
        idName[temp] = item[3]
        idDirector[temp] = item[1]
        idActor[temp] = item[2]
        if item[1].__len__() == 4 or item[2].__len__() == 4:
            re = item[0].strip().strip("'")
            idwithoutActor.add(re)

    csvfile = open("../../../data/NewRawData/basicTreat.csv", "r", encoding="utf-8")
    reader = csv.reader(csvfile)
    create_csv()
    content = "id", "title", "director", "actors", "year", "month", "day", "weekday", "version", "tag", "rate", "reviewNum", "five", "four", "three", "two", "one"
    write_csv(content)
    i = 0
    for line in reader:
        i = i + 1
        if i % 1000 == 0:
            print(i)
        if line[4] == "0" or line[5] == "0" or line[6] == "0" or line[7] == "0" or line[4] == "year" \
                or line[0] in idwithoutActor:
            continue
        result = line
        result[1] = idName[line[0]]
        result[3] = idActor[line[0]]
        result[2] = idDirector[line[0]]
        # print(result)
        write_csv(result)
