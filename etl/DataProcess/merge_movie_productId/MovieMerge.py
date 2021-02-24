import csv
import pandas as pd
import lxml
import os
from bs4 import BeautifulSoup

fileUrl = "MergeMovie.csv"
errorUrl = "errorMovie.csv"
folderUrl = "E:/K/tongji/personal/Learning/semester 5/DataWarehouse/Amazon/results/c000"


def all_path(dirname):
    result = []
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            result.append(apath)
    return result


def create_csv():
    path = "../../data/raw/" + fileUrl
    with open(path, 'w') as f:
        csv_write = csv.writer(f)


def write_csv(content):
    path = "../../data/raw/" + fileUrl
    with open(path, 'a+', newline='', encoding='utf-8') as f:
        csv_write = csv.writer(f)
        data_row = content
        csv_write.writerow(data_row)


def create_errorcsv():
    path = "../../data/raw/" + errorUrl
    with open(path, 'w') as f:
        csv_write = csv.writer(f)


def write_errorcsv(content):
    path = "../../data/raw/" + errorUrl
    with open(path, 'a+', newline='', encoding='utf-8') as f:
        csv_write = csv.writer(f)
        data_row = content
        csv_write.writerow(data_row)


class UnionFindSet(object):

    def __init__(self, data_list):
        self.father_dict = {}
        self.size_dict = {}

        for node in data_list:
            self.father_dict[node] = node
            self.size_dict[node] = 1

    def find(self, node):
        father = self.father_dict[node]
        if (node != father):
            if father != self.father_dict[father]:  # 在降低树高优化时，确保父节点大小字典正确
                self.size_dict[father] -= 1
            father = self.find(father)
        self.father_dict[node] = father
        return father

    def is_same_set(self, node_a, node_b):
        """查看两个节点是不是在一个集合里面"""
        return self.find(node_a) == self.find(node_b)

    def union(self, node_a, node_b):
        """将两个集合合并在一起"""
        if node_a is None or node_b is None:
            return

        a_head = self.find(node_a)
        b_head = self.find(node_b)

        if (a_head != b_head):
            a_set_size = self.size_dict[a_head]
            b_set_size = self.size_dict[b_head]
            if a_set_size >= b_set_size:
                self.father_dict[b_head] = a_head
                self.size_dict[a_head] = a_set_size + b_set_size
            else:
                self.father_dict[a_head] = b_head
                self.size_dict[b_head] = a_set_size + b_set_size


idSet = set()
create_errorcsv()

csvFile = open("../../../data/MergedData/mergedData.csv", "r", encoding="utf-8")
idReader = csv.reader(csvFile)
for item in idReader:
    idSet.add(item[0])

union_find_set = UnionFindSet(idSet)

# 在这里插入解析html的代码

# 读取文件
fileSet = set()
errorFile = set()

tempFileSet = all_path("E:\\K\\tongji\\personal\\Learning\\semester 5\\DataWarehouse\\Amazon\\results\\result")
for item in tempFileSet:
    fileSet.add(item.replace("\\", "/"))

# 解析
i = 0
for item in fileSet:
    i = i + 1
    if i % 1000 == 0:
        print(i)
    htmlid = item[89:99]
    # print(htmlid)
    content = open(item, 'r', encoding="utf-8").read()
    soup = BeautifulSoup(content, 'lxml')
    try:
        a_list = soup.find(id="MediaMatrix").find_all('a')
        pre_id = ''
        for a_tag in a_list:
            href = a_tag['href']
            if len(href.split('/dp/')) > 1:
                cor_id = href.split('/dp/')[1][0:10]
                if cor_id != pre_id and cor_id in idSet:
                    pre_id = cor_id
                    # print(pre_id,cor_id)
                    union_find_set.union(htmlid, cor_id)
    except:
        print("error:", item)
        lin = item, "html"
        write_errorcsv(lin)

# 并入并查集

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
    if res_dict[item].__len__() > 1:
        write_csv(res_dict[item])
