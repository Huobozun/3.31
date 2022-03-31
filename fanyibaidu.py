import csv

import http.client
import hashlib
from urllib import parse
import random
import time,re


def baidufanyi(word):

    appid = '20220321001133747'
    secretKey = '7UyMiEds7BCrDAoDjjBd'
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q =word
    fromLang = 'en'
    toLang = 'zh'
    salt = random.randint(32768, 65536)
    sign = appid+q+str(salt)+secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode(encoding='utf-8'))
    sign = m1.hexdigest()
    myurl = myurl+'?appid='+appid+'&q='+parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign 

    #file = open('result.txt','w')
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        response = httpClient.getresponse()
        _str = response.read().decode('utf-8')
        _str = eval(_str)
        #print(_str['trans_result'])
        if(len(_str['trans_result'])==1):
            xx3=[]
            xx1=_str['trans_result']
            xx2=xx1[0]
            xx3.append(xx2['dst'])
        else:
            xx1=_str['trans_result']
            xx3=[]
            for i in range(0,len(xx1)):
                xx2=xx1[i]
                xx3.append(xx2['dst'])
        #print(xx3)
    except Exception as e:
        #print('2',e)
        time.sleep(2)#0.7在range0-3可以进行
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        response = httpClient.getresponse()
        _str = response.read().decode('utf-8')
        _str = eval(_str)
        #print(_str)
        if(len(_str['trans_result'])==1):
            xx3=[]
            xx1=_str['trans_result']
            xx2=xx1[0]
            xx3.append(xx2['dst'])
        else:
            xx1=_str['trans_result']
            xx3=[]
            for i in range(0,len(xx1)):
                xx2=xx1[i]
                xx3.append(xx2['dst'])
        #print(xx3)
    finally:
        if httpClient:
            httpClient.close()
    #file.close()
    return xx3

#将相应文件需要翻译的词每行的list为一个元素形成list放入a中
"""_path="/home/zjg/code2/file/Diseasr_or_Syndrome_All_AGGREGATED.tsv"
a=getword(_path)

#求数量
num=0
for i in range(0,len(a)):
    b=a[i]
    for j in range(0,len(b)):
        c=b[j]
        num+=len(c)
print(num)"""

#写入文件，包括英文和译文
"""with open('result-fanyi.tsv','w',newline='')as f:
    for i in range(0,20):#写入20行内容
        af=a[i]
        for j in range(0,len(af)):
            #print(af[i])
            rf=baidufanyi(af[j])
            tsv_w=csv.writer(f,delimiter=' ')
            str5=(af[j],rf)
            tsv_w.writerow(str5)
f.close()
"""

