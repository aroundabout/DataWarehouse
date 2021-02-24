import csv
import regex

url = "../data/NewRawData/NameFormatData.csv"


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


def word_joint(ffirstHalf, rroundBrackets, ssquareBrackets):
    rresult = ffirstHalf
    for iitem in rroundBrackets:
        rresult += '(' + iitem + ')'
    for iitem in ssquareBrackets:
        rresult += iitem
    return rresult


result = set()
keyWord = set()

for line in open('../../../res/HighFrequencyWords.txt', 'r', encoding='utf-8'):
    keyWord.add(line.strip('\n').strip())

csvFile = open("../../../data/NewRawData/FormatData.csv", "r", encoding='utf-8')
reader = csv.reader(csvFile)
create_csv()
i = 0
for line in reader:
    i = i + 1
    if i % 1000 == 0:
        print(i)
    name = line[1]
    roundBrackets = regex.findall(r'\(((?:[^()]+|(?R))+)\)', name)
    squareBrackets = regex.findall(r"\[.+?\]", name)
    firstHalf = regex.sub(u"\\[.*?]|\\{.*?}|\\(.*?\\)", "", name).strip()

    # 除了之后再()[]中，还要注意在fitsthalf中的部分比如editiion之类的
    if '-' in firstHalf:
        ans = firstHalf.split('-', 1)
        for key in keyWord:
            if len(ans) > 1 and key in ans[1]:
                firstHalf = ans[0].strip()
                break
    # 年份就不管了
    for key in keyWord:
        for item in roundBrackets:
            if key in item:
                roundBrackets.remove(item)
            if item.isdigit():
                roundBrackets.remove(item)
        for item in squareBrackets:
            if key in item:
                squareBrackets.remove(item)
            if item.isdigit():
                squareBrackets.remove(item)

    temp = word_joint(firstHalf, roundBrackets, squareBrackets)
    line[1] = temp
    content = line
    write_csv(content)
