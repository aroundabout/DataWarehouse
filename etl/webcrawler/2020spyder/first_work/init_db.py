import redis
import csv
db = redis.StrictRedis(host='127.0.0.1', port=6379, decode_responses=True)
f= open('C:\\Users\\任冬晨\\Desktop\\productId.csv','r')
itemId=csv.reader(f)
reslut=list(itemId)
f.close()
for product in reslut:
    db.sadd('movieID', product[1])