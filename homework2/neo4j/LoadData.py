import csv

csvFile = open("review.csv", "w", encoding='utf-8', newline="")
writer = csv.writer(csvFile)

beFile = open("belong.csv", "w", encoding='utf-8', newline="")
b_writer = csv.writer(beFile)

user = {}
product = set()
movieName = set()


def write_review(_userId, _helpfulness, _score, _time, _productId):
    re = "REVIEW"
    if _productId == '' or _userId == '' or _helpfulness == '' or _score == -1.0 or _time == '':
        return
    writer.writerow([_userId, _helpfulness, _score, _time, _productId, re])


def write_user():
    u = "User"
    userFile = open("user.csv", "w", encoding='utf-8', newline="")
    u_writer = csv.writer(userFile)
    for key, value in user.items():
        u_writer.writerow([key, value, u])


def write_product():
    p = "Product"
    proFile = open("product.csv", "w", encoding='utf-8', newline="")
    p_writer = csv.writer(proFile)
    for i in product:
        p_writer.writerow([i, p])


def write_movie():
    m = "Movie"
    moFile = open("movie.csv", "w", encoding='utf-8', newline="")
    m_writer = csv.writer(moFile)
    for moviename in movieName:
        m_writer.writerow([moviename, m])


productId = ''
userId = ''
profileName = ''
helpfulness = ''
score = -1.0
time = ''

for line in open('../../clean_date/movies.txt', 'r', encoding='ISO-8859-1'):
    if 'review/summary: ' in line:
        continue
    if 'review/text: ' in line:
        continue
    if 'product/productId: ' in line:
        productId = line
        continue
    if 'review/userId: ' in line:
        userId = line
        continue
    if 'review/profileName: ' in line:
        profileName = line
        continue
    if 'review/helpfulness: ' in line:
        helpfulness = line
        continue
    if 'review/score: ' in line:
        score = line
        continue
    if 'review/time: ' in line:
        time = line
        productId = productId[len("product/productId: "):].strip("\n")
        userId = userId[len("review/userId: "):].strip("\n")
        profileName = profileName[len("review/profileName: "):].strip("\n")
        helpfulness = helpfulness[len("review/helpfulness: "):].strip("\n")
        score = score[len("review/score: "):].strip("\n")
        time = time[len("review/time: "):].strip("\n")
        # 处理user 和 product
        user[userId] = profileName
        product.add(productId)
        # 处理review，直接写
        write_review(userId, helpfulness, score, time, productId)
        # 重置
        productId = ''
        userId = ''
        profileName = ''
        helpfulness = ''
        score = -1.0
        time = ''

with open('../../clean_date/product_info.csv', 'r', encoding='utf-8') as pifile:
    pireader = csv.reader(pifile)
    mname = [row[0] for row in pireader]
    mname=mname[1:]
    for item in mname:
        movieName.add(item)

with open('../../clean_date/product_info.csv', 'r', encoding='utf-8') as pifile:
    ppireader = csv.reader(pifile)
    ppid = [row[1] for row in ppireader]
    ppid=ppid[1:]

for index in range(len(ppid)):
    b = "Belong"
    if ppid[index] in product and mname[index] in movieName:
        b_writer.writerow([ppid[index], mname[index], b])

write_user()
write_product()
write_movie()
