import csv
import uuid


# 创建和写文件函数
def create_csv(filename):
    path = "../../../data/neo4j/" + filename
    with open(path, 'w') as f:
        csv_write = csv.writer(f)


def write_csv(c, filename):
    path = "../../../data/neo4j/" + filename
    with open(path, 'a+', newline='', encoding='utf-8') as f:
        csv_write = csv.writer(f)
        data_row = c
        csv_write.writerow(data_row)


if __name__ == "__main__":

    titleSet = set()
    genreSet = set()
    actorSet = set()
    directorSet = set()
    id_yearDict = {}
    id_monthDict = {}
    id_dayDict = {}
    id_weekdayDict = {}
    id_seasonDict = {}
    id_yearmonthDict = {}
    id_yearseasonDict = {}
    id_monthdayDict = {}
    id_yearmonthdayDict = {}
    id_titleDict = {}
    id_versionDict = {}
    title_directorDict = {}
    title_actorDict = {}
    actor_acotrDict = {}
    actor_directorDict = {}
    title_genreDict = {}
    title_rateDict = {}
    title_reviewNumDict = {}
    title_fiveDict = {}
    title_fourDict = {}
    title_threeDict = {}
    title_twoDict = {}
    title_oneDict = {}

    yearid = {}
    monthid = {}
    dayid = {}
    weekdayid = {}
    seasonid = {}
    yearmonthid = {}
    yearseasonid = {}
    monthdayid = {}
    yearmonthdayid = {}
    titleid = {}
    directorid = {}
    actorid = {}
    genreid = {}
    rateid = {}
    numberid = {}


    def createProduct():

        genreFile = open("../../../data/raw/genre.txt", "r", encoding="utf-8")
        genreReader = csv.reader(genreFile)
        for genreItem in genreReader:
            if genreItem[0] != "":
                genreSet.add(genreItem[0])

        headername = "product-header.csv"
        create_csv(headername)
        content = "ProductId:ID", "Title", "Director", "Actor", "Year", "Month", "Day", "Weekday", "Version", "Tag", "Rate", "ReviewNum", "Five", "Four", "Three", "Two", "One", ":LABEL"
        write_csv(content, headername)

        print("data load finish")

        filename = "product.csv"
        create_csv(filename)
        productFile = open("../../../data/result/last.csv", "r", encoding="utf-8")
        productReader = csv.reader(productFile)
        cnt = 0
        for productItem in productReader:
            cnt = cnt + 1
            if cnt % 1000 == 0:
                print(cnt)
            if productReader.line_num == 1:
                continue
            if productItem[1] == "The Passion of the Christ":
                continue
            titleSet.add(productItem[1])
            content = productItem[0], productItem[1], productItem[2], productItem[3], productItem[4], productItem[5], \
                      productItem[6], productItem[7], productItem[8], productItem[9], productItem[10], productItem[11], \
                      productItem[12], productItem[13], productItem[14], productItem[15], productItem[16], "Product"
            dire = productItem[2].strip("{").strip("}").split(",")
            for d in dire:
                rrrres = d.strip().strip("'")
                if rrrres != '':
                    directorSet.add(rrrres)
            act = productItem[3].strip("{").strip("}").split(",")
            for a in act:
                resss = a.strip().strip("'")
                if resss != '':
                    actorSet.add(resss)
            write_csv(content, filename)
        print("createProduct")


    def createYear():
        headername = "year-header.csv"
        create_csv(headername)
        content = "Yearid:ID", "Year", ":LABEL"
        write_csv(content, headername)
        filename = "year.csv"
        create_csv(filename)
        for i in range(1931, 2100):
            idd = uuid.uuid1()
            yearid[i] = idd
            content = idd, i, "Year"
            write_csv(content, filename)
        print("createYear")


    def createMonth():
        headername = "month-header.csv"
        create_csv(headername)
        content = "Monthid:ID", "Month", ":LABEL"
        write_csv(content, headername)
        filename = "month.csv"
        create_csv(filename)
        for i in range(1, 13):
            idd = uuid.uuid1()
            monthid[i] = idd
            content = idd, i, "Month"
            write_csv(content, filename)
        print("createMonth")


    def createDay():
        headername = "day-header.csv"
        create_csv(headername)
        content = "Dayid:ID", "Day", ":LABEL"
        write_csv(content, headername)
        filename = "day.csv"
        create_csv(filename)
        for i in range(1, 32):
            idd = uuid.uuid1()
            dayid[i] = idd
            content = idd, i, "Day"
            write_csv(content, filename)
        print("createDay")


    def createWeekDay():
        headername = "weekday-header.csv"
        create_csv(headername)
        content = "Weekdayid:ID", "Weekday", ":LABEL"
        write_csv(content, headername)
        filename = "Weekday.csv"
        create_csv(filename)
        for i in range(1, 8):
            idd = uuid.uuid1()
            weekdayid[i] = idd
            content = idd, i, "Weekday"
            write_csv(content, filename)
        print("createWeekday")


    def createSeason():
        headername = "season-header.csv"
        create_csv(headername)
        content = "Seasonid:ID", "Season", ":LABEL"
        write_csv(content, headername)
        filename = "season.csv"
        create_csv(filename)
        for i in range(1, 5):
            idd = uuid.uuid1()
            seasonid[i] = idd
            content = idd, i, "Season"
            write_csv(content, filename)
        print("createSeason")


    def createYearMonth():
        headername = "yearmonth-header.csv"
        create_csv(headername)
        content = "Yearmonthid:ID", "Yearmonth", ":LABEL"
        write_csv(content, headername)
        filename = "yearmonth.csv"
        create_csv(filename)
        for i in range(1931, 2100):
            for j in range(1, 13):
                idd = uuid.uuid1()
                result = str(i) + "." + str(j)
                yearmonthid[result] = idd
                content = idd, result, "Yearmonth"
                write_csv(content, filename)
        print("createYearMonth")


    def createYearSeason():
        headername = "yearseason-header.csv"
        create_csv(headername)
        content = "Yearseasonid:ID", "Yearseason", ":LABEL"
        write_csv(content, headername)
        filename = "yearseason.csv"
        create_csv(filename)
        for i in range(1931, 2100):
            for j in range(1, 5):
                idd = uuid.uuid1()
                result = str(i) + "." + str(j)
                yearseasonid[result] = idd
                content = idd, result, "Yearseason"
                write_csv(content, filename)
        print("createYearSeason")


    def createMonthDay():
        headername = "monthday-header.csv"
        create_csv(headername)
        content = "Monthdayid:ID", "Monthday" ":LABEL"
        write_csv(content, headername)
        filename = "monthday.csv"
        create_csv(filename)
        for i in range(1, 13):
            for j in range(1, 32):
                idd = uuid.uuid1()
                result = str(i) + "." + str(j)
                monthdayid[result] = idd
                content = idd, result, "Monthday"
                write_csv(content, filename)
        print("createMonthDay")


    # def createYearMonthDay():
    #     headername = "yearmonthday-header.csv"
    #     create_csv(headername)
    #     content = "Yearmonthdayid:ID", "Yearmonthday", ":LABEL"
    #     write_csv(content, headername)
    #     filename = "yearmonthday.csv"
    #     create_csv(filename)
    #     for i in range(1931, 2100):
    #         for j in range(1, 32):
    #             for k in range(1, 32):
    #                 idd = uuid.uuid1()
    #                 result = str(i) + "." + str(j) + "." + str(k)
    #                 yearmonthdayid[result] = idd
    #                 content = idd, result, "YearMonthDay"
    #                 write_csv(content, filename)
    #     print("createYearMonthDay")

    def createTitle():
        headername = "title-header.csv"
        create_csv(headername)
        content = "Titleid:ID", "Title", ":LABEL"
        write_csv(content, headername)
        filename = "title.csv"
        create_csv(filename)
        for item in titleSet:
            if item != '':
                idd = uuid.uuid1()
                titleid[item] = idd
                content = idd, item, "Title"
                write_csv(content, filename)
        print("createTitle")


    def createDirector():
        headername = "director-header.csv"
        create_csv(headername)
        content = "Directorid:ID", "Director", ":LABEL"
        write_csv(content, headername)
        filename = "director.csv"
        create_csv(filename)
        for item in directorSet:
            if item != '':
                idd = uuid.uuid1()
                directorid[item] = idd
                content = idd, item, "Director"
                write_csv(content, filename)
        print("createDirector")


    def createActor():
        headername = "actor-header.csv"
        create_csv(headername)
        content = "Actorid:ID", "Actor", ":LABEL"
        write_csv(content, headername)
        filename = "actor.csv"
        create_csv(filename)
        for item in actorSet:
            if item != '':
                idd = uuid.uuid1()
                actorid[item] = idd
                content = idd, item, "Actor"
                write_csv(content, filename)
        print("createActor")


    def createGenre():
        headername = "genre-header.csv"
        create_csv(headername)
        content = "Genreid:ID", "Genre", ":LABEL"
        write_csv(content, headername)
        filename = "genre.csv"
        create_csv(filename)
        for item in genreSet:
            if item != '':
                idd = uuid.uuid1()
                genreid[item] = idd
                content = idd, item, "Genre"
                write_csv(content, filename)
        print("createGenre")


    def createRate():
        headername = "rate-header.csv"
        create_csv(headername)
        content = "Rateid:ID", "Rate", ":LABEL"
        write_csv(content, headername)
        filename = "rate.csv"
        create_csv(filename)
        for i in range(1, 51):
            idd = uuid.uuid1()
            rateid[i / 10] = idd
            content = idd, i / 10, "Rate"
            write_csv(content, filename)
        print("createRate")


    def createNumber():
        headername = "number-header.csv"
        create_csv(headername)
        content = "Numberid:ID", "Number", ":LABEL"
        write_csv(content, headername)
        filename = "number.csv"
        create_csv(filename)
        for i in range(1, 6):
            idd = uuid.uuid1()
            numberid[i] = idd
            content = idd, i, "Number"
            write_csv(content, filename)
        print("createNumber")


    def createNode():
        createProduct()
        createYear()
        createMonth()
        createDay()
        createWeekDay()
        createSeason()
        createYearMonth()
        createMonthDay()
        # createYearMonthDay()
        createYearSeason()
        createTitle()
        createDirector()
        createActor()
        createGenre()
        createRate()
        createNumber()


    def ProductId_Year():
        headername = "productId_year-header.csv"
        create_csv(headername)
        content = ":START_ID", ":END_ID", ":TYPE"
        write_csv(content, headername)
        filename = "productId_year.csv"
        create_csv(filename)
        for key in id_yearDict.keys():
            content = key, yearid[id_yearDict[key]], "ProductId_Year"
            write_csv(content, filename)
        print("ProductId_Year")


    def ProductId_Month():
        headername = "productId_month-header.csv"
        create_csv(headername)
        content = ":START_ID", ":END_ID", ":TYPE"
        write_csv(content, headername)
        filename = "productId_month.csv"
        create_csv(filename)
        for key in id_monthDict.keys():
            content = key, monthid[id_monthDict[key]], "ProductId_Month"
            write_csv(content, filename)
        print("ProductId_Month")


    def ProductId_Day():
        headername = "productId_day-header.csv"
        create_csv(headername)
        content = ":START_ID", ":END_ID", ":TYPE"
        write_csv(content, headername)
        filename = "productId_day.csv"
        create_csv(filename)
        for key in id_dayDict.keys():
            content = key, dayid[id_dayDict[key]], "ProductId_Day"
            write_csv(content, filename)
        print("ProductId_Day")


    def ProductId_WeekDay():
        headername = "productId_weekday-header.csv"
        create_csv(headername)
        content = ":START_ID", ":END_ID", ":TYPE"
        write_csv(content, headername)
        filename = "productId_weekday.csv"
        create_csv(filename)
        for key in id_weekdayDict.keys():
            content = key, weekdayid[id_weekdayDict[key]], "ProductId_Weekday"
            write_csv(content, filename)
        print("ProductId_Weekday")


    def ProductId_Season():
        headername = "productId_season-header.csv"
        create_csv(headername)
        content = ":START_ID", ":END_ID", ":TYPE"
        write_csv(content, headername)
        filename = "productId_season.csv"
        create_csv(filename)
        for key in id_seasonDict.keys():
            content = key, seasonid[id_seasonDict[key]], "ProductId_Season"
            write_csv(content, filename)
        print("ProductId_Season")


    def ProductId_YearMonth():
        headername = "productId_yearmonth-header.csv"
        create_csv(headername)
        content = ":START_ID", ":END_ID", ":TYPE"
        write_csv(content, headername)
        filename = "productId_yearmonth.csv"
        create_csv(filename)
        for key in id_yearmonthDict.keys():
            content = key, yearmonthid[id_yearmonthDict[key]], "ProductId_Yearmonth"
            write_csv(content, filename)
        print("ProductId_Yearmonth")


    def ProductId_YearSeason():
        headername = "productId_yearseason-header.csv"
        create_csv(headername)
        content = ":START_ID", ":END_ID", ":TYPE"
        write_csv(content, headername)
        filename = "productId_yearseason.csv"
        create_csv(filename)
        for key in id_yearseasonDict.keys():
            content = key, yearseasonid[id_yearseasonDict[key]], "ProductId_Yearseason"
            write_csv(content, filename)
        print("ProductId_Yearseason")


    def ProductId_MonthDay():
        headername = "productId_monthday-header.csv"
        create_csv(headername)
        content = ":START_ID", ":END_ID", ":TYPE"
        write_csv(content, headername)
        filename = "productId_monthday.csv"
        create_csv(filename)
        for key in id_monthdayDict.keys():
            content = key, monthdayid[id_monthdayDict[key]], "ProductId_Monthday"
            write_csv(content, filename)
        print("ProductId_Monthday")


    # def ProductId_YearMonthDay():
    #     headername = "productId_yearmonthday-header.csv"
    #     create_csv(headername)
    #     content = ":START_ID", ":END_ID", ":TYPE"
    #     write_csv(content, headername)
    #     filename = "productId_yearmonthday.csv"
    #     create_csv(filename)
    #     for key in id_yearmonthdayDict.keys():
    #         content = key, yearmonthdayid[id_yearmonthdayDict[key]], "ProductId_Yearmonthday"
    #         write_csv(content, filename)
    #     print("ProductId_Yearmonthday")

    def Title_ProductId():
        headername = "productid_title-header.csv"
        create_csv(headername)
        content = ":START_ID", ":END_ID", ":TYPE"
        write_csv(content, headername)
        filename = "productid_title.csv"
        create_csv(filename)
        for key in id_titleDict.keys():
            if id_titleDict[key] != '':
                content = key, titleid[id_titleDict[key]], "Productid_Title"
                write_csv(content, filename)
        print("Title_Productid")


    def Director_Title():
        headername = "title_director-header.csv"
        create_csv(headername)
        content = ":START_ID", ":END_ID", ":TYPE"
        write_csv(content, headername)
        filename = "title_director.csv"
        create_csv(filename)
        for key in title_directorDict.keys():
            temp = title_directorDict[key].strip("{").strip("}").split(",")
            for item in temp:
                result = item.strip().strip("'")
                if result != '' and key != '':
                    content = titleid[key], directorid[result], "Title_Director"
                    write_csv(content, filename)
        print("title_director")


    def Actor_Title():
        headername = "title_actor-header.csv"
        create_csv(headername)
        content = ":START_ID", ":END_ID", ":TYPE"
        write_csv(content, headername)
        filename = "title_actor.csv"
        create_csv(filename)
        for key in title_actorDict.keys():
            temp = title_actorDict[key].strip("{").strip("}").split(",")
            for item in temp:
                result = item.strip().strip("'")
                if result != '' and key != '':
                    content = titleid[key], actorid[result], "Title_Actor"
                    write_csv(content, filename)
        print("Title_Actor")


    def Genre_Title():
        headername = "title_genre-header.csv"
        create_csv(headername)
        content = ":START_ID", ":END_ID", ":TYPE"
        write_csv(content, headername)
        filename = "title_genre.csv"
        create_csv(filename)
        for key in title_genreDict.keys():
            temp = title_genreDict[key].strip("{").strip("}").split(",")
            for item in temp:
                result = item.strip().strip("'")
                if result != '' and key != '':
                    content = titleid[key], genreid[result], "Title_Genre"
                    write_csv(content, filename)
        print("Title_genre")


    def Title_rate():
        headername = "title_rate-header.csv"
        create_csv(headername)
        content = ":START_ID", ":END_ID", ":TYPE"
        write_csv(content, headername)
        filename = "title_rate.csv"
        create_csv(filename)
        for key in title_rateDict.keys():
            if title_rateDict[key] != '' and key != '':
                content = titleid[key], rateid[title_rateDict[key]], "Title_Rate"
                write_csv(content, filename)
        print("Title_Rate")


    def Title_Number():
        headername = "title_number-header.csv"
        create_csv(headername)
        content = ":START_ID", "Number", ":END_ID", ":TYPE"
        write_csv(content, headername)
        filename = "title_number.csv"
        create_csv(filename)
        for key in title_fiveDict.keys():
            if key != '':
                result = int(title_fiveDict[key])
                if result > 0:
                    content = titleid[key], result, numberid[5], "Title_Number"
                    write_csv(content, filename)
        for key in title_fourDict.keys():
            if key != '':
                result = int(title_fourDict[key])
                if result > 0:
                    content = titleid[key], result, numberid[4], "Title_Number"
                    write_csv(content, filename)
        for key in title_threeDict.keys():
            if key != '':
                result = int(title_threeDict[key])
                if result > 0:
                    content = titleid[key], result, numberid[3], "Title_Number"
                    write_csv(content, filename)
        for key in title_twoDict.keys():
            if key != '':
                result = int(title_twoDict[key])
                if result > 0:
                    content = titleid[key], result, numberid[2], "Title_Number"
                    write_csv(content, filename)
        for key in title_oneDict.keys():
            if key != '':
                result = int(title_oneDict[key])
                if result > 0:
                    content = titleid[key], result, numberid[1], "Title_Number"
                    write_csv(content, filename)
        print("Title_Number")


    def Actor_Actor():
        headername = "actor_actor-header.csv"
        create_csv(headername)
        content = ":START_ID", "Title", ":END_ID", ":TYPE"
        write_csv(content, headername)
        filename = "actor_actor.csv"
        create_csv(filename)
        for key in title_actorDict.keys():
            temp = title_actorDict[key].strip("{").strip("}").split(",")
            for i in range(0, len(temp)):
                for j in range(i + 1, len(temp)):
                    result1 = temp[i].strip().strip("'")
                    result2 = temp[j].strip().strip("'")
                    if result1 != '' and result2 != '':
                        content = actorid[result1], key, actorid[result2], "Actor_Actor"
                        write_csv(content, filename)
        print("Actor_Actor")


    def Actor_Director():
        headername = "director_actor-header.csv"
        create_csv(headername)
        content = ":START_ID", "Title", ":END_ID", ":TYPE"
        write_csv(content, headername)
        filename = "director_actor.csv"
        create_csv(filename)
        for key in title_directorDict.keys():
            temp1 = title_directorDict[key].strip("{").strip("}").split(",")
            temp2 = title_actorDict[key].strip("{").strip("}").split(",")
            for i in temp1:
                for j in temp2:
                    result1 = i.strip().strip("'")
                    result2 = j.strip().strip("'")
                    if result1 != '' and result2 != '':
                        content = directorid[result1], key, actorid[result2], "Director_Actor"
                        write_csv(content, filename)
        print("Director_Actor")


    def createRelationship():
        productFile = open("../../../data/result/last.csv", "r", encoding="utf-8")
        productReader = csv.reader(productFile)
        for productItem in productReader:
            if productReader.line_num == 1:
                continue
            if productItem[1] == "The Passion of the Christ":
                continue
            # 跟着id走
            pid = productItem[0]
            title = productItem[1]
            year = int(productItem[4])
            month = int(productItem[5])
            day = int(productItem[6])
            weekday = int(productItem[7])
            version = productItem[8]
            season = 1
            if month == 1 or month == 2 or month == 3:
                season = 1
            elif month == 4 or month == 5 or month == 6:
                season = 2
            elif month == 7 or month == 8 or month == 9:
                season = 3
            elif month == 10 or month == 11 or month == 12:
                season = 4
            # 跟着title走
            director = productItem[2]
            actor = productItem[3]
            tag = productItem[9]
            rate = productItem[10]
            reviewNum = productItem[11]
            five = productItem[12]
            four = productItem[13]
            three = productItem[14]
            two = productItem[15]
            one = productItem[16]

            id_yearDict[pid] = year
            id_monthDict[pid] = month
            id_dayDict[pid] = day
            id_weekdayDict[pid] = weekday
            id_seasonDict[pid] = season
            id_yearmonthDict[pid] = str(year) + "." + str(month)
            id_yearseasonDict[pid] = str(year) + "." + str(season)
            id_monthdayDict[pid] = str(month) + "." + str(day)
            id_yearmonthdayDict[pid] = str(year) + "." + str(month) + "." + str(day)
            id_titleDict[pid] = title
            id_versionDict[pid] = version
            if title in title_directorDict.keys():
                continue
            else:
                title_directorDict[title] = director
                title_actorDict[title] = actor
                title_genreDict[title] = tag
                if rate != '':
                    title_rateDict[title] = float(rate)
                title_reviewNumDict[title] = reviewNum
                title_fiveDict[title] = five
                title_fourDict[title] = four
                title_threeDict[title] = three
                title_twoDict[title] = two
                title_oneDict[title] = one

        Title_ProductId()
        Director_Title()
        Actor_Title()
        Genre_Title()
        Actor_Director()
        Actor_Actor()
        Title_rate()
        Title_Number()
        ProductId_Year()
        ProductId_Month()
        ProductId_Day()
        ProductId_WeekDay()
        ProductId_Season()
        ProductId_YearMonth()
        ProductId_YearSeason()
        ProductId_MonthDay()
        # ProductId_YearMonthDay()


    createNode()
    createRelationship()
