import csv
import numpy as np
from src.etl.merge_movie_productId.Union import UnionFindSet

url = "../../../data/raw/updateMergedMovie.csv"


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


if __name__ == "__main__":

    idSet = set()
    copyFIle = open("../../../data/NewRawData/copy_basicTreat.csv", "r", encoding="utf-8")
    copyReader = csv.reader(copyFIle)
    for item in copyReader:
        idSet.add(item[0])

    union_find_set = UnionFindSet(idSet)

    mergedFile = open("../../../data/raw/MergeMovie.csv", "r", encoding="utf-8")
    mergedReader = csv.reader(mergedFile)
    for item in mergedReader:
        if item[0] not in idSet:
            continue
        for theid in item:
            if theid in idSet:
                union_find_set.union(item[0], theid)
    proid = []
    title = []
    director = []
    csvFile = open("../../../data/NewRawData/basicTreat.csv", "r", encoding="utf-8")
    reader = csv.reader(csvFile)
    for item in reader:
        proid.append(item[0])
        title.append(item[1])
        director.append(item[2])

    # for item in title:
    searchTitle = np.array(title)
    searchDirector = np.array(director)
    counttttt = 0
    for item in searchTitle:
        counttttt = counttttt + 1
        if counttttt % 1000 == 0:
            print(counttttt)
        eq_letter = np.where(searchTitle == item)
        temp = []
        for inde in eq_letter[0]:
            temp.append(inde)
        # print(temp.__len__())
        if temp.__len__() == 1:
            continue
        else:
            for i in range(0, len(temp)):
                for j in range(i + 1, len(temp)):
                    # print(i, j)
                    if director[i] == director[j]:
                        union_find_set.union(proid[i], proid[j])

    res_dict = {}
    for i in union_find_set.father_dict:
        rootNode = union_find_set.find(i)
        if rootNode in res_dict:
            res_dict[rootNode].append(i)
        else:
            res_dict[rootNode] = [i]

    create_csv()
    keys = res_dict.keys()
    for item in keys:
        content = res_dict[item],
        write_csv(content)
