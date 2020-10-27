# 获取Amazon评论数据集中有多少个不同的电影

## 1.获取ProductID

* 由于movies.txt文件本身太大，使用UltraEdit打开文本，观察得到文本中'product/productId: '后面是所求的商品id

* 使用python，按行读取，进行字符串匹配获得productid，存入集合，输出在.csv中
```python
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
```

## 2.爬虫获取Product页面

1. 初步方案：

    * 使用python的request库进行网页的信息获取，再将获取的文本信息使用Beautiful Soup库进行解析，查找所需要的信息。
        
    * 使用技术：python request库，Beautiful Soup库
        
    * 在最初使用此方案时，能够正常获取信息。但由于amazon的反爬虫机制，获取效率在短时间内就大幅度下降，大部分时候只能访问到验证码界面。
    
2. 改良方案：

    * 在学习了解了amazon的反爬虫机制后，使用更换ip地址，随机请求头生成来进行伪装，使用了现成的proxy_pool工具，利用爬虫对免费的代理ip网址进行定时爬取ip并检验，维护一个可用的代理ip池，每次请求从ip池随机取出一个进行ip代理访问。
    
    * 使用技术：proxy_pool，Redis数据库
        
    * 在使用改良方案后，被amazon识别的次数有效降低了，但爬取速度对于25w的数据量稍显不足。
    
3. 再次改进：

    * 利用python的多线程和多进程功能提高爬虫并发度，使cpu资源全部被利用，加快爬取速度。
    
    * 使用技术：python thread和multiprocess库

4. 再次改进：

    * 将所有url导入Redis数据库，每次获取时随机取出访问，访问失败再放回数据库中。
    
    * 使用request库进行页面的内容获取，利用beautiful soup进行页面解析，分析页面内容获取电影名。
        
    * 在爬虫运行时，另开进程进行代理ip池的维护，同样将可用代理ip存储于Redis数据库中，每次访问时利用代理ip池中的可用ip进行代理，同时使用fake_useragent库对请求的浏览器进行随机的变更，模拟是不同的用户在访问。
    
    * 再利用多进程和多线程并发最大化电脑的cpu利用率，提高爬取速度。

    



## 3.页面分析

1. 分析标题内容

    * 观察标题，发现在标题内的商品信息是多于电影名本身，如[VHS]等，为了更加有效的分析这些词，选择建立高频词词库，优先分析出现频率高的单词或词组
    
    * 建立起词库之后开始对于词库内容分析，里面的词大致可以分成以下几个部分
    
        * 常用词 the a of 等没有实际意义的词
    
        * 商品类别，如VHS、Blu-ray等
        
        * 国家，地区
        
        * 年份，时间，是否为重制版
        
        * 是否分级，是哪种剪辑版（如导演剪辑版）
        
        * 哪种特定的版本
        
        * 是否为合集
        
        * 宝莱坞\好莱坞出品
        
        * collection pack表示合集
        
        * 一些关键属于表示电视剧或者动漫的第几季或者第几集或者第几卷
        
    * 根据一定的判定是否为同一部电影的原则，筛选出其中与电影版本本身无关的内容，加入高频词词库HighFrequencyWords.txt。大致原则如下：
        
        1. 商品的载体，如VHS，Blu-ray，XXX screen，3D等与是否为同一部电影无关
        
        1. 商品是否为Amazon独占与是否为同一部电影无关
        
        2. 商品的版本，如xxx edition等与是否为同一部电影无关

        3. 商品的播出载体，如for psp等于是否为同一部电影无关
        
        3. 商品有几张disc与是否为同一部电影无关
        
        4. 商品中标注为宝莱坞的与是否为同一部电影无关
        
        4. 商品是否属于Hallmark Hall of Fame与是否为同一电影无关
        
        4. 商品是否为XX周年庆与是否为同一部电影无关
        
        5. 不同国家、地区的版本收到当地出版要求限制，认为是不同的电影，但是不同语言字幕认为还是同一部电影
        
        6. 同一部电影标注为不同年份，认为是不同的电影
        
        7. 同一部电影，标注为重制版，认为是不同的电影
        
        8. 同一部电影，是否分级，是否为导演或其他人的剪辑版也认为是不同的电影
        
        9. 名字中出现合集collection和pack的情况有大概率内涵多部电影，对于字段拆分得到多部电影
        
    * 将电视剧，动漫等属于加入词库ErrorWord.txt，遇到带有这些词的名字可以直接删除
        
2. 标题处理

    * 根据该上述原则对于电影名进行处理
    
        * 若存在ErrorWord.txt中的词汇则直接进行删除
        
        * 根据观察，商品名主要分成三个部分，主体，()内部分，[]内部分，使用正则表达式对字符串拆分处理
        
        ```python
            name = line.strip('\n').strip(',').strip('\"')
            roundBrackets = regex.findall(r'\(((?:[^()]+|(?R))+)\)', name)
            squareBrackets = regex.findall(r"\[.+?\]", name)
            firstHalf = regex.sub(u"\\[.*?]|\\{.*?}|\\(.*?\\)", "", name).strip()
        ```
      
        * 在主体部分，类似的关键词存在于 '-' 符号后面，于是对于主体再次分割，并且观测后半部分是否有高频词，若有，则保留前半部分
        
        ```python
            if '-' in firstHalf:
                ans = firstHalf.split('-', 1)
                for key in keyWord:
                    if len(ans) > 1 and key in ans[1]:
                        firstHalf = ans[0].strip()
                        break
        ``` 
      
        * 对于()和[]内的部分使用相同的手法操作，存在高频词则删除，防止干扰电影的一致性判断
        
         ```python
             for key in keyWord:
                for item in roundBrackets:
                    if key in item:
                        roundBrackets.remove(item)
                for item in squareBrackets:
                    if key in item:
                        squareBrackets.remove(item)
         ```       
        
        * 对于合集处理
        
            1. 检测名字中是否有Collection或Pack等关键词，若存在，则先检测()在检测主体部分（经过观察，[]中不存在多个电影名，不做检测）中是否有'/'或','存在，若有，则做字符串切割并加入集合中
            
            ```python
                if 'Collection' in name or 'Pack' in name:
                    isGet = False
                    for item in roundBrackets:
                        # 去除括号 根据/和,分割字符串 去除空格 加入pack
                        if '/' in item:
                            isGet = True
                            tmp = item.strip('(').strip(')')
                            tmp = tmp.split('/')
                            for content in tmp:
                                if '(' in content and ')' not in content:
                                    result.add(content.strip() + ')')
                                else:
                                    result.add(content.strip())
                        elif ',' in item:
                            isGet = True
                            tmp = item.strip('(').strip(')')
                            tmp = tmp.split(',')
                            for content in tmp:
                                if '(' in content and ')' not in content:
                                    result.add(content.strip() + ')')
                                else:
                                    result.add(content.strip())
                    if not isGet:
                        t = firstHalf.split(':', 1)
                        if ('Collection' in t[0] or 'Pack' in t[0]) and len(t) > 1:
                            t = t[1].split('/')
                            for content in t:
                                result.add(content.strip())
            ```
            
            2. 在经过后续其他部分的处理之后，若()和[]中没有内容了，且主体中还有'/'则再对主体进行切割（不对于','切割的理由是根据随机统计没有collection的时候','分割多个电影名的情况较少，同时可能切割到正常的电影名）
         
            ```python
                if '/' in firstHalf and len(roundBrackets) == 0 and len(squareBrackets) == 0:
                t = temp.split('/')
                for item in t:
                    result.add(item.strip())
            ```
         
        * 重新拼接
            
            在完成了上述的步骤之后，按照主体 () []的顺序重新拼接，重新检测是否可能为电影集合并重新切割，将结果加入result集合,输出len(result)得到结果
        