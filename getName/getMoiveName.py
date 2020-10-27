# 关于怎么处理电影名字的初步方案

# 电影时长不能超过

# 主要的字符床处理对象是() []内步的内容
# UFC直接滚 拳击赛


# 考虑加入高频词
# 建立词库

# 关于一部电影的情况
# 以下认为是与电影内容无关，只与商品质量、表达形式（for psp这种）有关的如 [VHS] [Blu-ray] (The Criterion Collection) (Widescreen Edition) (EP mode) (DVD) [UMD for PSP] (Deluxe Extended Edition) (Legendary Collection)
# 还有宝莱坞相关的关键词
# tv show 这种也不是电影
# season感觉可以全滚了 part不能全滚
# 通过高频词筛选出与电影无关的词
# 对于类似内容，包括在括号内存在多个VHS blue ray这种名字的混合的情况，直接删除对应的[] 和 ()
# 其次是年份的处理，在这里认为不同的年份的电影是不同的，同理，重制版 re Remastered等关键词意味着电影是不同的 予以保留
# 其次是国家的处理，括号内含如 CN UK USA表示电影在不同的国家或者地区，根据不同的审核规则，电影的内容也不完全相同，认为是不同的电影
# 关于括号内是相同电影名字的不同翻译的情况，这里认为可以直接删除，理由如下
# 若存在另一个商品名字为同一电影的不同翻译，则一般可以认为是面向另一国家的出版物，处理原则与上文相同，认为是不同的电影
# 不同配音可以直接删
# unrated 和rated 有没有分级也认为是不同电影
# vol认为是不同的卷，认为是不同的电影
# 导演剪辑版和普通版不是一个 其他的剪辑版本也认为是不同的电影
# 3d和2d认为是一部电影

# 关于电影合集的情况
# 在商品中存在电影合集，在这种情况下，无视商品本身的名字，直接读取括号内的字符串，根据 / 符号或者其他类似意义的符号分割字符串，获得电影名字
# 当名字里面有collection的时候

# 关于处理结束后如何存放电影名以及计数的问题
# 将处理过后的电影名放入集合set中防止重复计数，再完成后直接读取set的长度得到结果，然后将set的内容物输出在csv中

# 关于字符串的拆分与重新拼接
# 在拆开字符串并完成处理之后，安装圆括号、方括号的顺序拼接，多个圆括号方括号按照原顺序拼接，在拆开的过程中删除各个部分之间的空格，拼接的过程中不予保留


# key word to delete   [VHS] [Blu-ray] (The Criterion Collection) (Widescreen Edition) (EP mode) (DVD) [UMD for PSP] (Deluxe Extended Edition) (Legendary Collection)
# 除了一些括号表示特别收藏版之类的，括号里面还有其他语言翻译的名字，可以认为是另一个版本的电影，收到各个国家的政策影响，认为不同语言版本也是不同的电影
# Remastered 重制版认为是新的电影
# 引号也要删掉"" ''
# 另外，不同的vol也认为是不同的movie
# 认为年份不同也是不同的电影
# 标题中表示商品为电影合集，电影数量无法统计
# the letter 和the letter(1994) 这种怎么算还不知道


# 总之先删除首尾的 '' ""

import csv
import regex


def create_csv():
    path = "NewName.csv"
    with open(path, 'w') as f:
        csv_write = csv.writer(f)


def write_csv(number, content):
    path = "NewName.csv"
    with open(path, 'a+', newline='', encoding='utf-8') as f:
        csv_write = csv.writer(f)
        data_row = [content]
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
        targetString1 = regex.findall(r'\(((?:[^()]+|(?R))+)\)', newName)
        targetString2 = regex.findall(r"\[.+?\]", newName)
        if len(targetString1) > 0:
            for item in targetString1:
                # 排除年份
                # if "/" in item:
                #     continue
                newItem = item.strip('(').strip(')').strip().replace('-', '').replace('/', '')
                if newItem.isdigit():
                    continue
                # print(item)
                result.add(item)
        if len(targetString2) > 0:
            for item in targetString2:
                #  print(item)
                # if "/" in item:
                #     continue
                newItem = item.strip('[').strip(']').strip().replace('-', '').replace('/', '')
                if newItem.isdigit():
                    continue
                result.add(item)

    # print(result.__len__())
    # 有7375个内容

    # for item in result:
    #     print(item)
    print(len(result))
    # 排除年份有7215个关键词
    # 排除年份中有- / 的之后还有7183
    # 有年份和国家混合的，不同国家地区的认为是不同的电影
    # 删除全部的 / 还有5502


def removeOuterParentheses(S: str) -> str:
    n = len(S)
    if 0 == n:
        return ""
    res = ""
    tmp = ['(']
    for i in range(1, n):
        if '(' == S[i]:
            if len(tmp) != 0:
                res += '('
            tmp.append('(')
        else:
            if 1 == len(tmp):
                del tmp[0]
            else:
                if '(' == tmp[-1]:
                    del tmp[-1]
                else:
                    tmp.append(')')
                res += ')'
    return res


def word_joint(firstHalf, roundBrackets, squareBrackets):
    result = firstHalf
    for item in roundBrackets:
        result += '(' + item + ')'
    for item in squareBrackets:
        result += item
    # print(result)

    return result


def get_name():
    result = set()
    keyWord = set()
    errorWord = set()
    # 读取词库
    for line in open('HighFrequencyWords.txt', 'r', encoding='utf-8'):
        keyWord.add(line.strip('\n').strip())
    for line in open('ErrorWord.txt', 'r', encoding='utf-8'):
        errorWord.add(line.strip('\n').strip())
    for line in open('productName.csv', 'r', encoding='utf-8'):
        # 字符串拆分
        name = line.strip('\n').strip(',').strip('\"')
        roundBrackets = regex.findall(r'\(((?:[^()]+|(?R))+)\)', name)
        squareBrackets = regex.findall(r"\[.+?\]", name)
        firstHalf = regex.sub(u"\\[.*?]|\\{.*?}|\\(.*?\\)", "", name).strip()

        # 杀一些不可能是电影的
        isFilm = True
        for eWord in errorWord:
            if eWord in name:
                isFilm = False
        if not isFilm:
            continue
        # 清除高频词
        # 除了之后再()[]中，还要注意在fitsthalf中的部分比如editiion之类的

        if '-' in firstHalf:
            ans = firstHalf.split('-', 1)
            for key in keyWord:
                if len(ans) > 1 and key in ans[1]:
                    firstHalf = ans[0].strip()
                    break

        for key in keyWord:
            for item in roundBrackets:
                if key in item:
                    roundBrackets.remove(item)
            for item in squareBrackets:
                if key in item:
                    squareBrackets.remove(item)
        # 处理合集
        # 可能还需要处理pack
        if 'Collection' in name or 'Pack' in name:
            isGet = False
            for item in roundBrackets:
                # 去除括号 根据/和,分割字符串 去除空格 加入pack
                if '/' in item:
                    isGet = True
                    tmp = item.strip('(').strip(')')
                    tmp = tmp.split('/')
                    for content in tmp:
                        if '(' in content and ')' not in content:
                            result.add(content.strip() + ')')
                        else:
                            result.add(content.strip())
                elif ',' in item:
                    isGet = True
                    tmp = item.strip('(').strip(')')
                    tmp = tmp.split(',')
                    for content in tmp:
                        if '(' in content and ')' not in content:
                            result.add(content.strip() + ')')
                        else:
                            result.add(content.strip())
            if not isGet:
                t = firstHalf.split(':', 1)
                if ('Collection' in t[0] or 'Pack' in t[0]) and len(t) > 1:
                    t = t[1].split('/')
                    for content in t:
                        result.add(content.strip())
        else:
            temp = word_joint(firstHalf, roundBrackets, squareBrackets)
            if '/' in firstHalf and len(roundBrackets) == 0 and len(squareBrackets) == 0:
                t = temp.split('/')
                for item in t:
                    result.add(item.strip())
            else:
                result.add(temp)
        # 这里处理结束之后可能需要回头再看一下多部电影的情况
    create_csv()
    for item in result:
        print(item)
        write_csv(0, item)
    print(len(result))


# get_key_word()


get_name()
