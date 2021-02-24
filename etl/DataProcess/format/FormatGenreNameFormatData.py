import csv
import Levenshtein

url = "../../../data/NewRawData/basicTreat.csv"


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
    create_csv()
    firstLine = "id", "title", "director", "actors", "year", "month", "day", "weekday", "version", "tag", "rate", "reviewNum", "five", "four", "three", "two", "one"
    write_csv(firstLine)
    genSet = set()
    errGenSet = set()
    translateGen = {}
    errorWord = set()
    tranGenFile = open("../../../data/translate/genTranslate.csv", "r", encoding="utf-8")
    tranGenReader = csv.reader(tranGenFile)
    for item in tranGenReader:
        translateGen[item[0].lower()] = item[1].lower()

    genlistFile = open("../../../data/raw/genre.txt", "r", encoding="utf-8")
    gen = csv.reader(genlistFile)
    for item in gen:
        genSet.add(item[0])
    # print(genSet)

    errGenListFile = open("../../../data/raw/errorgenre.txt", "r", encoding="utf-8")
    errGen = csv.reader(errGenListFile)
    for item in errGen:
        errGenSet.add(item[0])
    # print(errGenSet)

    csvFile = open("../../../data/NewRawData/GenreNameFormatData.csv", "r", encoding="utf-8")
    reader = csv.reader(csvFile)

    for line in open('../../../data/dataInHW1/ErrorWord.txt', 'r', encoding='utf-8'):
        errorWord.add(line.strip('\n').strip())

    count = 0
    iiiiiii = 0
    for item in reader:
        iiiiiii = iiiiiii + 1
        if iiiiiii % 1000 == 0:
            print(iiiiiii)
        result = item
        isFilm = True
        for eWord in errorWord:
            if eWord in item[1]:
                isFilm = False
        if not isFilm:
            continue
        flag = 1
        detailGen = set()
        temp = item[9].strip("[").strip("]").lower().split(",")
        for i in temp:
            target = i.strip().strip("'")
            # print(target)
            if target in translateGen.keys():
                target = translateGen[target]
            target = target.split("and")
            for iiitem in target:
                ttarget = iiitem.split("&")
                for splited in ttarget:
                    tWord = splited.strip()
                    # print(tWord)
                    for err in errGenSet:
                        if Levenshtein.distance(err, tWord) < 3:
                            flag = 0
                            break
                    for genre in genSet:
                        if Levenshtein.distance(genre, tWord) < 3:
                            detailGen.add(genre)
        if flag == 1:
            if detailGen.__len__() > 0:
                count = count + 1
                # print(detailGen)
                result[9] = detailGen
                write_csv(result)

    print(count)
