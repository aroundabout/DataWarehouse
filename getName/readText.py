# 文件用于读取movies.txt
import csv


def create_csv():
    path = "productId.csv"
    with open(path, 'w') as f:
        csv_write = csv.writer(f)


def write_csv(number, Pid):
    path = "productId.csv"
    with open(path, 'a+', newline='') as f:
        csv_write = csv.writer(f)
        data_row = [number, Pid]
        csv_write.writerow(data_row)


i = 0
lastLine = ''
create_csv()
result = set()
for line in open('movies.txt', 'r', encoding='ISO-8859-1'):
    if line[0:19] == 'product/productId: ':
        newLine = line[19:29]
        result.add(newLine)
for item in result:
    write_csv(i, item)
    i += 1
