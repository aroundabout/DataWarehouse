import csv

csvFile = open("../../clean_date/clean_movies.csv", "r", encoding='utf-8')
reader = csv.reader(csvFile)
result = {}
length = 0
for item in reader:
    if reader.line_num == 1:
        continue
    length += len(item[1].split(','))

csvFile.close()

print(length)
