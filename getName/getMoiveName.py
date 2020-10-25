import csv
import re


# key word to delete   [VHS] [Blu-ray] (The Criterion Collection) (Widescreen Edition) (EP mode) (DVD) [UMD for PSP] (Deluxe Extended Edition) (Legendary Collection)
# 除了一些括号表示特别收藏版之类的，括号里面还有其他语言翻译的名字，可以认为是另一个版本的电影，收到各个国家的政策影响，认为不同语言版本也是不同的电影
# Remastered 重制版认为是新的电影
# 引号也要删掉"" ''
# 另外，不同的vol也认为是不同的movie
# 认为年份不同也是不同的电影
# 总之先删除首尾的 '' ""

def create_csv():
    path = "NewName.csv"
    with open(path, 'w') as f:
        csv_write = csv.writer(f)


def write_csv(number, Pid):
    path = "NewName.csv"
    with open(path, 'a+', newline='', encoding='utf-8') as f:
        csv_write = csv.writer(f)
        data_row = [Pid]
        csv_write.writerow(data_row)


def delete_quotation():
    create_csv()
    i = 0
    for line in open('productName.csv', 'r', encoding='utf-8'):
        newName = line.strip('\n').strip(',').strip('\"')
        print(newName)
        write_csv(i, newName)
        i += 1


# delete_quotation()

# csvFile = open('NewName.csv', 'r',encoding='utf-8')
# reader = csv.reader(csvFile)
# for item in reader:

# 使用正则表达式获取() []之间的内容
# 使用集合保存里面的内容

def get_key_word():
    result = set()

    for line in open('productName.csv', 'r', encoding='utf-8'):
        newName = line.strip('\n').strip(',').strip('\"')
        targetString1 = re.findall(r"\(.+?\)", newName)
        targetString2 = re.findall(r"\[.+?\]", newName)
        if len(targetString1) > 0:
            for item in targetString1:
                # 排除年份
                newItem = item.strip('(').strip(')').replace('-', '').replace('/', '')
                if newItem.isdigit():
                    continue
                # print(item)
                result.add(item)
        if len(targetString2) > 0:
            for item in targetString2:
                #  print(item)
                newItem = item.strip('[').strip(']')
                if newItem.isdigit():
                    continue
                result.add(item)

    # print(result.__len__())
    # 有7375个内容

    for item in result:
        print(item)
    print(len(result))
    # 排除年份有7215个关键词
    # 排除年份中有- / 的之后还有7184


get_key_word()
