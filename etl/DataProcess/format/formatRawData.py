import csv

url = "../../../data/NewRawData/FormatData.csv"


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


reviewNum = {}
five = {}
four = {}
three = {}
two = {}
one = {}

rawData = open("../../../data/NewRawData/rawData.csv", "r", encoding='utf-8')
rawDataReader = csv.reader(rawData)

reviewData = open("../../../data/dataInHW2/review.csv", "r", encoding='utf-8')
reviewDataReader = csv.reader(reviewData)

for line in rawDataReader:
    reviewNum[line[0]] = 0
    five[line[0]] = 0
    four[line[0]] = 0
    three[line[0]] = 0
    two[line[0]] = 0
    one[line[0]] = 0

print("review id load success")

i = 0

for line in reviewDataReader:
    i = i + 1
    if i % 10000 == 0:
        print(i)
    productId = line[4]
    score = float(line[2])
    if productId in reviewNum.keys():
        reviewNum[productId] = reviewNum[productId] + 1
        if score == 1:
            one[productId] = one[productId] + 1
        elif score == 2:
            two[productId] = two[productId] + 1
        elif score == 3:
            three[productId] = three[productId] + 1
        elif score == 4:
            four[productId] = four[productId] + 1
        elif score == 5:
            five[productId] = five[productId] + 1
    else:
        reviewNum[productId] = 1
        if score == 1:
            one[productId] = 1
            two[productId] = 0
            three[productId] = 0
            four[productId] = 0
            five[productId] = 0
        elif score == 2:
            one[productId] = 0
            two[productId] = 1
            three[productId] = 0
            four[productId] = 0
            five[productId] = 0
        elif score == 3:
            one[productId] = 0
            two[productId] = 0
            three[productId] = 1
            four[productId] = 0
            five[productId] = 0
        elif score == 4:
            one[productId] = 0
            two[productId] = 0
            three[productId] = 0
            four[productId] = 1
            five[productId] = 0
        elif score == 5:
            one[productId] = 0
            two[productId] = 0
            three[productId] = 0
            four[productId] = 0
            five[productId] = 1

create_csv()

print("data load success!")

firstLine = "id", "title", "director", "actors", "year", "month", "day", "weekday", "version", "tag", "rate", "reviewNum", "five", "four", "three", "two", "one"
write_csv(firstLine)


rawData = open("../../../data/NewRawData/rawData.csv", "r", encoding='utf-8')
rawDataReader = csv.reader(rawData)
i = 0
for line in rawDataReader:
    i = i + 1
    if rawDataReader.line_num == 1:
        continue
    if i % 1000 == 0:
        print(i)
    tag = line[27].split("›")
    newline = line[0], line[1], line[10], line[11], line[3], line[4], line[5], line[6], line[19], tag, line[20], \
              reviewNum[line[0]], five[line[0]], four[line[0]], three[line[0]], two[line[0]], one[line[0]]
    write_csv(newline)
