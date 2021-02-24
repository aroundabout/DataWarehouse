#从selenium里面导入webdriver
import csv
import random
import multiprocessing
import time
import gc
import redis
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


PROCESS_NUM=16
def connect_to_web():
    #指定chrom的驱动
    #执行到这里的时候Selenium会到指定的路径将chrome driver程序运行起来
    db = redis.StrictRedis(host='127.0.0.1', port=6379, decode_responses=True)
    option = webdriver.ChromeOptions()
    option.add_argument("--lang=en")
    option.add_argument('--ignore-certificate-errors') 
    option.add_argument('--ignore-ssl-errors') 
    #option.add_argument('headless')  # 设置option
    driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',options=option)
    #get 方法 打开指定网址
    itemUrl=db.spop("movieID")
    driver.get('https://www.amazon.com/dp/'+itemUrl)
    time.sleep(random.random()*3)
    #选择网页元素
    try:
        title = driver.find_element_by_id('productTitle').text
    except:
        try:
            title=driver.find_element_by_css_selector("[class='_1GTSsh _2Q73m9']").text
        except:
            db.sadd("moviID",itemUrl)
            driver.quit()
            for x in list(locals().keys())[:]:
                del locals()[x]
            gc.collect()
            return
    db.sadd("movieName",title)
    driver.quit()
    for x in list(locals().keys())[:]:
                del locals()[x]
    gc.collect()
    return



if __name__ == "__main__":
    a=time.time()
    for i in range(250000):
        while len(multiprocessing.active_children()) > PROCESS_NUM: # Change
            t = 5 * random.random()
            if t < 0.5:
                t += 1.5
            elif t > 3.5:
                t -= 2.5
            time.sleep(t)
        t = multiprocessing.Process(target=connect_to_web, args=())
        t.start()
        time.sleep(random.random()/3+0.3)
        if i%300==1 and i>300:
            time.sleep(30)
    while len(multiprocessing.active_children()) > 1 : # Wait the thread I created to finish
        time.sleep(2)
    b=time.time()
    print('------------Finish-----------')
    print(b-a)
    





        







































