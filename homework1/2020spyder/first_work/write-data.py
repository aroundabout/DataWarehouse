import redis
import csv


db = redis.StrictRedis(host='127.0.0.1', port=6379, decode_responses=True)
f= open('./productName.csv','w',encoding='utf-8',newline='')
csv_write=csv.writer(f)
nameList=list(db.smembers("movieName"))
for name in nameList:
    csv_write.writerow([name,''])