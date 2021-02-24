import csv
import calendar
from datetime import datetime

url = "../data/raw/rawdata4.csv"


# 创建和写文件函数
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


title = {}
rate = {}
languages = {}
year = {}
month = {}
day = {}
weekday = {}
movieType = {}
director = {}
actor = {}

# 信息有title,productId,rate,binding,runtime,languages,release_year,release_month,release_day,release_weekday
# 还差类型、导演、演员
# infoOne = open("../data/clean_date/product_info.csv", "r", encoding='utf-8')
# reader = csv.reader(infoOne)
# for item in reader:
#     if reader.line_num == 1:
#         continue
#     title[item[1]] = item[0]
#     rate[item[1]] = item[2]
#     languages[item[1]] = item[5]
#     year[item[1]] = item[6]
#     month[item[1]] = item[7]
#     day[item[1]] = item[8]
#     weekday[item[1]] = item[9]
#     movieType[item[1]] = ''
#     director[item[1]] = ''
#     actor[item[1]] = ''

infoTwo = open("NameFormatData.csv", "r", encoding='utf-8')
readerTwo = csv.reader(infoTwo)
for item in readerTwo:
    productId = item[0]
    # 标题
    title[productId] = item[1]
    # 评分
    r = item[8]
    nr = r.split(" ", 1)
    rate[productId] = nr[0]
    # 语言
    languages[productId] = item[6]
    # 时间
    onTime = item[7]
    print(onTime)
    if onTime != '':
        if onTime.isdigit():
            year[productId] = onTime
            month[productId] = 0
            day[productId] = 0
            weekday[productId] = 0
        elif '.' in onTime:
            year[productId] = onTime.split('.', 1)[0]
            month[productId] = 0
            day[productId] = 0
            weekday[productId] = 0
        else:
            try:
                t = datetime.strptime(onTime, '%B %d, %Y')
                # %B %d, %Y
                y = t.strftime("%Y")
                m = int(t.strftime("%m"))
                d = int(t.strftime("%d"))
                year[productId] = y
                month[productId] = m
                day[productId] = d
                weekday[productId] = calendar.weekday(y, m, d)
            except BaseException:
                year[productId] = 0
                month[productId] = 0
                day[productId] = 0
                weekday[productId] = 0
    else:
        year[productId] = 0
        month[productId] = 0
        day[productId] = 0
        weekday[productId] = 0
    director[productId] = item[2]
    actor[productId] = item[3]
    movieType[productId] = item[4]

print("info two load finish")
#



# print("load dat success")
#
# create_csv()
# line = "productId", "title", "rate", "languages", "year", "month", "day", "weekday", "type", "director", "actor"
# write_csv(line)
# for key in title:
#     try:
#         # if movieType[key] == '' and listtype.__contains__(title[key]):
#         #     movieType[key] = listtype[title[key]]
#         # if director[key] == '' and listdirect.__contains__(title[key]):
#         #     director[key] = listdirect[title[key]]
#         # if actor[key] == '' and listactor.__contains__(title[key]):
#         #     actor[key] = listactor[title[key]]
#         content = key, title[key], rate[key], languages[key], year[key], month[key], day[key], weekday[key], movieType[
#             key], director[key], actor[key]
#         write_csv(content)
#     except BaseException:
#         print(key)












# listdirect = {}
# listactor = {}
# listtype = {}
#
# infoDirect = open("../data/clean_date/movie_director.csv", "r", encoding='utf-8')
# readerDirect = csv.reader(infoDirect)
#
# infoActor = open("../data/clean_date/movie_actor.csv", "r", encoding='utf-8')
# readerActor = csv.reader(infoActor)
#
# infoType = open("../data/clean_date/movie_genre.csv", "r", encoding='utf-8')
# readerType = csv.reader(infoType)
#
# for item in infoDirect:
#     temp = item.split(",")
#     key = temp[0]
#     value = temp[1]
#     if listactor.__contains__(key):
#         listdirect[key] = listdirect[key] + "," + value
#     else:
#         listdirect[key] = value
#
#
# for item in infoActor:
#     temp = item.split(",")
#     key = temp[0]
#     value = temp[1]
#     if listactor.__contains__(key):
#         listactor[key] = listactor[key] + "," + value
#     else:
#         listactor[key] = value
#
#
# for item in infoType:
#     temp = item.split(",")
#     key = temp[0]
#     value = temp[1]
#     if listtype.__contains__(key):
#         listtype[key] = listtype[key] + "," + value
#     else:
#         listtype[key] = value




