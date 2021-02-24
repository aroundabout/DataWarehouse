import csv
import hashlib
import json
import time
import random
import requests

appID = '20210101000660586'
# 你的密钥
secretKey = 'TxnnntKjlOUjWPg_Psye'
# 百度翻译 API 的 HTTP 接口
apiURL = 'http://api.fanyi.baidu.com/api/trans/vip/translate'


def baiduAPI_translate(query_str, to_lang):
    '''
    传入待翻译的字符串和目标语言类型，请求 apiURL，自动检测传入的语言类型获得翻译结果
    :param query_str: 待翻译的字符串
    :param to_lang: 目标语言类型
    :return: 翻译结果字典
    '''
    # 生成随机的 salt 值
    salt = str(random.randint(32768, 65536))
    # 准备计算 sign 值需要的字符串
    pre_sign = appID + query_str + salt + secretKey
    # 计算 md5 生成 sign
    sign = hashlib.md5(pre_sign.encode()).hexdigest()
    # 请求 apiURL 所有需要的参数
    params = {
        'q': query_str,
        'from': 'auto',
        'to': to_lang,
        'appid': appID,
        'salt': salt,
        'sign': sign
    }
    try:
        # 直接将 params 和 apiURL 一起传入 requests.get() 函数
        response = requests.get(apiURL, params=params)
        # 获取返回的 json 数据
        result_dict = response.json()
        # 得到的结果正常则 return
        if 'trans_result' in result_dict:
            return result_dict
        else:
            print('Some errors occured:\n', result_dict)
    except Exception as e:
        print('Some errors occured: ', e)


def baiduAPI_translate_main(query_str, dst_lang=''):
    '''
    解析翻译结果后输出，默认实现英汉互译
    :param query_str: 待翻译的字符串，必填
    :param dst_lang: 目标语言类型，可缺省
    :return: 翻译后的字符串
    '''
    if dst_lang:
        # 指定了目标语言类型，则直接翻译成指定语言
        result_dict = baiduAPI_translate(query_str, dst_lang)
    else:
        # 未指定目标语言类型，则默认进行英汉互译
        result_dict = baiduAPI_translate(query_str, 'zh')
        if result_dict['from'] == 'zh':
            result_dict = baiduAPI_translate(query_str, 'en')
    # 提取翻译结果字符串，并输出返回
    dst = result_dict['trans_result'][0]['dst']
    print('{}: {} -> {}: {}'.format(result_dict['from'], query_str, result_dict['to'], dst))
    return dst


# str=baiduAPI_translate_main('Infantil y familiar','en')
#
# print(str)


csvFile = open("../../../data/NewRawData/GenreNameFormatData.csv", "r", encoding="utf-8")
reader = csv.reader(csvFile)

Kset=set()

for line in reader:
    # print(line)
    temp = line[9].strip("[").strip("]").split(",")
    for item in temp:
        temp = item.strip().strip("'").split("&")
        for sItem in temp:
            ttemp = sItem.strip().split("and")
            for ssItem in ttemp:
                target = ssItem.strip()
                Kset.add(target)
