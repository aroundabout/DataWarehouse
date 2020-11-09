import requests
import time
import threading
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import random
import redis
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
'''
cookies=[]
cookie1="session-id=143-2773384-1720133; sp-cdn='L5Z9:CN'; ubid-main=135-3206192-1605513; lc-main=en_US; x-main='ISMB?ssTGeZUJXZ4hhAM2ARryDHPH98ViXfQOzsTa6MVIyh@y789@bsVxACBOOR4'; at-main=Atza|IwEBIEYZlKQxUZ1vE98uGtCmIY9VJjIglwK8QYZM9ENesXfs6VSI5fYkdxKk-A44B-ivbNw9XkgR11yVqbhmuzRfMHST3RmdRnXbIHsOHcCNNlvCEsEzpRSTmP0mtdppLch-JSwFxnZ1_ce2FqGdYD5lA3ZxHONovMDQHhiIxHW47eJA-0-cNJyh-aTLCaXV7hQMCton5qc1Dbs7VWvvKodYso7p; sess-at-main='frecMCBRdjgdO2SH76rAnAehjVjU5W+mzHkIBd65Xoo='; sst-main=Sst1|PQFvjwC-kQRB5ycxdFH1t485CRY-0kc0mR3zElU1c93ivI53yqtaJYQ3vxR9nNosBmpw5uc50BqD_Q3iAlYN_HC9nCkOM2qOMrbT2tzHMp47ocaI-gpBHdpEhJLrtm_CrYReipMwXz7sq7MU-X1guclyDgOXlUSRztQ-vtp15lkMBvbtabHbv_Ulj4k6JJUwyvy45OAW7kmXIymmCr43oDsONHRnFDkvyXdKG_koW0UeTTBbCvhc_WFI8hUH6bbK21I7NVwB7MxMSCbOrn3qObvw_g_2aaeDg3exbyqm05gXLbo; session-id-time=2082787201l; i18n-prefs=USD; session-token='9COiqUZL5jopxqKTvxDLyqJzajX/Hq4RRDSpnoXDRMG1VqT66CUXn4ltKWwN/lqwrdPHqWQVmP0Xzz+a0h2GcqSIJ26X8wOrcK5QUCst/ANsgbsXnLvaMEijqWNTlhphTRTrDtmfVQWi63zYUyy1dNcUkcecVPlnJeesDA4HYV2jPwrAwidNPsL/k0oxe0LHt0oF7XKQnj6guVBtdHSnwA=='; csm-hit=tb:s-YK3XDSG18Z09PMF84AWB|1603120207893&t:1603120209089&adb:adblk_no"
cookie2="session-id=143-2773384-1720133; sp-cdn='L5Z9:CN'; ubid-main=135-3206192-1605513; session-token=wjWG/gMOFp+Zr/z6TsNUuzLthmlArNBHnXRqmldpU6xh/wzL14g7hiPI1LoOV13EcuPWtG/or53KRWs1AfhLFlwTrc27uGPDlnfnZm+jvPtSwzEMP5Zrnl8BwCQPiKZWbv8jKGKLWkZyyIAmFGfiOpMwD5pfrICDgF6M8tvLd1r2o9fWYr5DneMY7ULbh3gmLtcyA+2KhrtNErBbLQa13VeU5aY5yLPj+RWpH09szvI0QtqCqtNCWlxODo88lM9PAFwAeDdpMqK7uVTs3ZeiaNjoVtTdAcDI; x-main='BUyhbbATK1EbrSIwXCDqC8a8h14Xyf7sCoe203cs4bSbwXaAnsR@5@O79h9L7RYJ'; at-main=Atza|IwEBIGyDCZ5sAPUvPXjvDh0y8ycTxsftdZgqV7MN7a4gGdc2dsPTK-8ebjUfpMQRu3sVBsl7PfktZ4qcEiNb6MWzlXTG7dQSHBYWrDcRoKSeUkXQZBdqfjFmNTSRgQPYfuoBhgVUA0MtF_r3xoVj_ogjLx35jXUb3bvDGXbti-wTjn4ueqMt36nmt_lV9vMxIGb_9AL6FxMHiEmIP8MUi0iWpA0w; sess-at-main='4NzGqEA2+nYzjLXoTKKysWcngTyrmuXBY1dEkFoJqVc='; sst-main=Sst1|PQGYGNJYKnJYsrvsdcwYQnrJCYoCdwA1jrpcU6gkhDzk_3t1WpaJaD9Qm2BPpTZSkJcdWXBL7HThxlrOzSBMlg7DyrBGXvLY7yosJn9ja2ssFlUE2g4c3xs09vMAxjr_wrcsElNc1ugnL-j231Y1ub7HSR6WVS0vumZ6ODlcexqk8Wnnv15e65BpjifvhpBJee8-9WYTDrdUea9eczPGqmtIYVp3CkM48y34aEruHQnq4q3QmHO4Y9kivzNyxqOGBSJVakwOk8UVy3i-wJsJYRmgwxKZUB1l9ZmoBfsTtjmSxR4; lc-main=en_US; session-id-time=2082787201l; i18n-prefs=USD; csm-hit=tb:s-YE27KKMDJX2N8T0RGS4H|1603120345953&t:1603120345953&adb:adblk_no"
cookie3="session-id=143-2773384-1720133; sp-cdn='L5Z9:CN'; ubid-main=135-3206192-1605513; lc-main=zh_CN; session-token=Z0HPw8I02igGA14/b2WnhiwMVUVZQvJqdPWQHFsm5g5I/7lUgWlUsh56YsvnP5mHws3tkZsewAYxtiCq+JpFoLQ+0qySKteS8tq7rKPq6BRw8AhVqPLwKxmL7vGB/yohAnIR9xP6/LYwibcDbW+wx/AF2sGOT4VPNcCLkRQWvxmj8MKlrXJdsvkUjYiqO2c/JOlazi2Q/fN9tLeR0h9nCrq0/aIuxfLss78zxYJ3jTq/ORVEJMvKRqxB823JUWz61J1fNxFlfetSQT54qmI4wLFAwcQrGaOo; x-main=lammV9mVno4cNlsuIv5dBSfaYx5mJxEljvOYc8maNy12QpcpfymEVfaYYRcFvqTj; at-main=Atza|IwEBIGNGeewD8MaSTwZTHJyNTKKhW4erJHQApWZjqb3A75I5CEOQiwYo-jrdxL9MyKgWOcGAUxPxZvBllvvUO8PVQ5FmMJvu2LJyOEaIyFNjmjby6s_q8mY-JCPUX4k-rEtOgELzBBo8dPmTy5OwUxqz2RwkXjCOBvwHIKySh3dDi2ZN9zbD9-yaufbRxnaDZiG0o9wiPagfprYef5UhsCPFLHKk; sess-at-main='TUmYMcVR1D91CyKxA/afF/cWvYFT11qqoPbztE2ZJ7Q='; sst-main=Sst1|PQHbzJbRUox1YT0kSvtr5NV5Ca5LgkZDf7-MKXqkEAG01BbCZwPwnZRU0FNBr2TaP3k_kkDZSXT0MBGpNKmNH6vgP-MRAqOOQT_QklQuYbADdeouRd5Clq3NOYi6764dXfcN_7epz7DzqAdaaAGqtHVA3EIb7dREwVg0H7G9WkxDuO2TgsOsU1edAHNH3ygsWLYmKLLTyLW8ByAfycy-xRgl87ou-CVebKKRYvzaaaSDQghLzvwG_bTWaev8jaOf_Eu4_nGZGxg3HC47VXZxJbmo-phondr4bm5XsURXEyMMSz8; session-id-time=2082787201l; i18n-prefs=USD; csm-hit=tb:s-0M6T524ZYK4TJ64A5ABD|1603120814880&t:1603120816884&adb:adblk_no"
'''
db = redis.StrictRedis(host='127.0.0.1', port=6379, decode_responses=True)
ua = UserAgent()
ip_dict = {}
ipPool=[]
THREAD_NUM=16
cout=0
IPurl="http://api.hailiangip.com:8422/api/getIp?type=1&num=30&pid=-1&unbindTime=300&cid=-1&orderId=O20102000012062693782&time=1603125464&sign=087140a9c701e6d96f86ced4b231c145&noDuplicate=0&dataType=0&lineSeparator=0&singleIp=0"
'''
def delete_proxy(p):
    requests.get('http://127.0.0.1:5010/delete?proxy=' + p)
'''
def get_proxy():  
    return random.choice(ipPool)


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
    #mycookie=cookies[random.randint(0,2)]
    try:
        p = get_proxy()
        proxier = { 'https' : 'http://' + p }
        response = requests.get(url, headers=header, proxies=proxier , timeout=10, verify=False)
        if response.status_code == 404:
            return
        elif response.status_code == 200: # get tittle
            Parser(response.text, movieID, p)
            return
        else:
            db.sadd('movieID', movieID)
            return       
    except Exception as e:
        if p in ip_dict:
            ip_dict[p] += 1
            if ip_dict[p] > 10:
                ip_dict.pop(p)
        else:
            ip_dict[p] = 1
        db.sadd('movieID', movieID)
        



def Parser(html, id, p):
    soup = BeautifulSoup(html, 'lxml')
    element = soup.find(id='productTitle')
    title = ''
    if element == None:
        element = soup.find('h1' ,attrs={'class': '_1GTSsh _2Q73m9'})
        if element == None: 
            # Error
            db.sadd('movieID', id)
            if p in ip_dict:
                ip_dict[p] += 1
                if ip_dict[p] > 10:
                    ip_dict.pop(p)
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
'''
def make_cookies():
    cookielist=[cookie1,cookie2,cookie3]
    for test in cookielist:
        temp={}
        test=test.split(';')
        for cookie in test:
            name,value = cookie.strip().split('=',1)
            temp[name] = value
        cookies.append(temp)
'''
def make_ProxyPool():
    while True:
        ip_str = requests.get(IPurl).text
        temp = json.loads(ip_str.strip())
        ips=temp['data']
        for ip in ips:
            t = ip["ip"]+":"+str(ip["port"])
            ipPool.append(t)
        time.sleep(150)
        ipPool.clear()
        ip_dict.clear()


if __name__ == '__main__':
    a=time.time()
    #make_cookies()
    t = threading.Thread(target=make_ProxyPool, args=())
    t.start()
    time.sleep(5)
    for i in range(250000):
        while threading.active_count() > THREAD_NUM: # Change
            t = 5 * random.random()
            if t < 0.5:
                t += 1.5
            elif t > 3.5:
                t -= 2.5
            time.sleep(t)
        t = threading.Thread(target=GetAndParse, args=())
        t.start()
        time.sleep(random.random()/3+0.3)
        if i%2500==1 and i>1000:
            time.sleep(30)
        


    while threading.active_count() > 2 : # Wait the thread I created to finish
        time.sleep(0.2)
    b=time.time()
    print('------------Finish-----------')
    print(b-a)
 

        

