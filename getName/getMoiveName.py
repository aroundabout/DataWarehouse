# 关于怎么处理电影名字的初步方案

# 主要的字符床处理对象是() []内步的内容
# 关于一部电影的情况
# 以下认为是与电影内容无关，只与商品质量、表达形式（for psp这种）有关的如 [VHS] [Blu-ray] (The Criterion Collection) (Widescreen Edition) (EP mode) (DVD) [UMD for PSP] (Deluxe Extended Edition) (Legendary Collection)
# 对于类似内容，包括在括号内存在多个VHS blue ray这种名字的混合的情况，直接删除对应的[] 和 ()
# 其次是年份的处理，在这里认为不同的年份的电影是不同的，同理，重制版 re Remastered等关键词意味着电影是不同的 予以保留
# 其次是国家的处理，括号内含如 CN UK USA表示电影在不同的国家或者地区放松，根据不同的审核规则，电影的内容也不完全相同，认为是不同的电影
# 关于括号内是相同电影名字的不同翻译的情况，这里认为可以直接删除，理由如下
# 若存在另一个商品名字为同一电影的不同翻译，则一般可以认为是面向另一国家的出版物，处理原则与上文相同，认为是不同的电影

# 关于电影合集的情况
# 在商品中存在电影合集，在这种情况下，无视商品本身的名字，直接读取括号内的字符串，根据 / 符号或者其他类似意义的符号分割字符串，获得电影名字

# 关于处理结束后如何存放电影名以及计数的问题
# 将处理过后的电影名放入集合set中防止重复计数，再完成后直接读取set的长度得到结果，然后将set的内容物输出在csv中


import csv
import re


# key word to delete   [VHS] [Blu-ray] (The Criterion Collection) (Widescreen Edition) (EP mode) (DVD) [UMD for PSP] (Deluxe Extended Edition) (Legendary Collection)
# 除了一些括号表示特别收藏版之类的，括号里面还有其他语言翻译的名字，可以认为是另一个版本的电影，收到各个国家的政策影响，认为不同语言版本也是不同的电影
# Remastered 重制版认为是新的电影
# 引号也要删掉"" ''
# 另外，不同的vol也认为是不同的movie
# 认为年份不同也是不同的电影
# 标题中表示商品为电影合集，电影数量无法统计
# the letter 和the letter(1994) 这种怎么算还不知道


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
                newItem = item.strip('(').strip(')').strip().replace('-', '').replace('/', '')
                if newItem.isdigit():
                    continue
                # print(item)
                result.add(item)
        if len(targetString2) > 0:
            for item in targetString2:
                #  print(item)
                newItem = item.strip('[').strip(']').strip().replace('-', '').replace('/', '')
                if newItem.isdigit():
                    continue
                result.add(item)

    # print(result.__len__())
    # 有7375个内容

    for item in result:
        print(item)
    print(len(result))
    # 排除年份有7215个关键词
    # 排除年份中有- / 的之后还有7183
    # 有年份和国家混合的，不同国家地区的认为是不同的电影


get_key_word()
