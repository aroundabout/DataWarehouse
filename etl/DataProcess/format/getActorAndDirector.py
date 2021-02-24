import csv
import Levenshtein

url = "../../../data/NewRawData/id_director_actor.csv"
urlA = "../../../data/NewRawData/actor.csv"
urlD = "../../../data/NewRawData/director.csv"


# 创建和写文件函数
# def create_csv():
#     path = url
#     with open(path, 'w') as f:
#         csv_write = csv.writer(f)
#
#
# def write_csv(c):
#     path = url
#     with open(path, 'a+', newline='', encoding='utf-8') as f:
#         csv_write = csv.writer(f)
#         data_row = c
#         csv_write.writerow(data_row)


# 创建和写文件函数
def create_csvD():
    path = urlD
    with open(path, 'w') as f:
        csv_write = csv.writer(f)


def write_csvD(c):
    path = urlD
    with open(path, 'a+', newline='', encoding='utf-8') as f:
        csv_write = csv.writer(f)
        data_row = c
        csv_write.writerow(data_row)


# 创建和写文件函数
def create_csvA():
    path = urlA
    with open(path, 'w') as f:
        csv_write = csv.writer(f)


def write_csvA(c):
    path = urlA
    with open(path, 'a+', newline='', encoding='utf-8') as f:
        csv_write = csv.writer(f)
        data_row = c
        csv_write.writerow(data_row)


if __name__ == "__main__":

    actor = {}
    director = {}
    name = {}
    actorSet = set()
    directorSet = set()
    # create_csv()
    # firstLine = "ids", "directors", "actors"

    resFile = open("../../../data/result/last.csv", "r", encoding="utf-8")
    resReader = csv.reader(resFile)
    for line in resReader:
        actor[line[0]] = line[3]
        director[line[0]] = line[2]
        name[line[0]] = line[1]

    csvFile = open("../../../data/raw/updateMergedMovie.csv", "r", encoding="utf-8")
    reader = csv.reader(csvFile)
    i = 0
    for line in reader:
        i = i + 1
        if i % 1000 == 0:
            print(i)
        idList = line[0].strip("[").strip("]").split(",")
        actorsss = set()
        directorsss = set()
        namesss = ''
        for item in idList:
            idItem = item.strip().strip("'").strip()
            if idItem not in actor.keys():
                continue
            actorList = actor[idItem].split(",")
            directorList = director[idItem].split(",")
            namesss = name[idItem]
            for actorItem in actorList:
                temp = actorItem.strip()
                tempactor = set()
                if len(actorsss) == 0:
                    actorsss.add(temp)
                    actorSet.add(temp)
                for actorI in actorsss:
                    if Levenshtein.distance(temp, actorI) > 5:
                        tempactor.add(temp)
                        actorSet.add(temp)
                for tempactorItem in tempactor:
                    actorsss.add(tempactorItem)
            for directorItem in directorList:
                temp = directorItem.strip()
                tempdirector = set()
                if len(directorsss) == 0:
                    directorsss.add(temp)
                    directorSet.add(temp)
                for directorI in directorsss:
                    if Levenshtein.distance(temp, directorI) > 5:
                        tempdirector.add(temp)
                        directorSet.add(temp)
                for tempdirectorItem in tempdirector:
                    directorsss.add(tempdirectorItem)
        for item in idList:
            content = item, directorsss, actorsss, namesss
            # write_csv(content)

    create_csvA()
    create_csvD()
    for ac in actorSet:
        content = ac,
        write_csvA(content)
    for di in directorSet:
        content = di,
        write_csvD(content)
