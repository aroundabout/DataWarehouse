import requests
import time
import multiprocessing
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import random
import redis
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

db = redis.StrictRedis(host='127.0.0.1', port=6379, decode_responses=True)
ua = UserAgent()
ip_dict = {}
Process_Number=16

def delete_proxy(p):
    requests.get('http://127.0.0.1:5010/delete?proxy=' + p)

def get_proxy():
    ip_str = requests.get("http://127.0.0.1:5010/get_all/").text
    ips = ip_str.strip()
    ips = ips[1:-1].strip()
    raw_ip_list = ips.split('\n')
    tmp = []
    for ip in raw_ip_list:
        t = ip.strip()
        t = t.strip(',')
        tmp.append(t.strip('"'))
    return random.choice(tmp)


def GetAndParse():
    header = {
        'User-Agent': ua.random,
        'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br'
    }
    movieID = db.spop('movieID')
    url = 'https://www.amazon.com/dp/' + movieID
    p = ''
    try:
        p = get_proxy()
        proxier = { 'https' : 'http://' + p }
        response = requests.get(url, headers=header, proxies=proxier , timeout=10, verify=False)       
    except:
        db.sadd('movieID', movieID)
    else:
        if response.status_code == 404:
            return
        elif response.status_code == 200: # get tittle
            Parser(response.text, movieID, p)
            return
        else:
            db.sadd('movieID', movieID)
            return



def Parser(html, id, p):
    soup = BeautifulSoup(html, 'lxml')
    element = soup.find(id='productTitle')
    title = ''
    if element == None:
        element = soup.find('h1' ,attrs={'class': '_1GTSsh _2Q73m9'})
        if element == None: # Error
            db.sadd('movieID', id)
            if p in ip_dict:
                ip_dict[p] += 1
                if ip_dict[p] > 10:
                    delete_proxy(p)
            else:
                ip_dict[p] = 1
            return False
        else: # Prime Video Page
            title = element.text
    else: # Simple Page
        title = element.text
    if 'Director' not in html: # A movie must have a director
        return False
    if 'Season' not in title and 'Season' in html: # TV show
        return False
    if 'Fitness' not in title and 'Fitness' in html: # Not a moive
        return False
    if 'Music Videos' in html:
        return False
    if 'Concerts' in html:
        return False
    db.sadd('movieName', title.strip())
    return True

if __name__ == "__main__":
    for i in range(250000):
        while multiprocessing.active_children()>Process_Number: # Change
            t = 5 * random.random()
            if t < 0.5:
                t += 1.5
            elif t > 3.5:
                t -= 2.5
            time.sleep(t)
        if i%2500 == 1 and i >10:
            time.sleep(30)
        p = multiprocessing.Process(target=GetAndParse)
        p.start()
        time.sleep(random.random()/3 + 0.2)
    while multiprocessing.active_children()>0:
        time.sleep(1)
    print('------------end-----------')



        
    
        

