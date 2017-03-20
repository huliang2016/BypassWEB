# coding=utf-8
import httplib
import urllib

__author__ = 'qinjiawei'

'''
绕过考试
'''
def Requestpost_question():

    for i in range(1, 8):
        print  i
        id = 5+i


        data = {'lessonId':id}
        data_encode = urllib.urlencode(data)

        requrl = '<url>?lessonId='+ str(id)
        refer = ""
        host = ''
        headerdata = {'Host':host,
                      'ApiKey':'',
                      'AuthToken':'',
                      'DeviceId':'',
                      'Origin':refer,
                      'Referer':refer,
                      'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        conn = httplib.HTTPConnection(host)
        conn.request(method="POST", url=requrl, body=data_encode, headers=headerdata)

        response = conn.getresponse()
        res = response.read()
        print res
'''
绕过视频
'''
def RequestPost_cal():
    id = 21652106 # 心跳包的id

    data = {'streamId':id}
    data_encode = urllib.urlencode(data)
    # requrl = 'http://api.dfsstv.cn/api/v1/Practice/Finish?lessonId='+ str(id)
    requrl = '<url>?streamId='+str(id)

    requrl = '<url>?lessonId='+ str(id)
    refer = ""
    host = ''
    headerdata = {'Host':host,
                  'ApiKey':'',
                  'AuthToken':'',
                  'DeviceId':'',
                  'Origin':refer,
                  'Referer':refer,
                  'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    conn = httplib.HTTPConnection(host)
    conn.request(method="POST", url=requrl, body=data_encode, headers=headerdata)

    response = conn.getresponse()
    res = response.read()
    print res
if __name__=="__main__":
    # Requestpost_question()
    RequestPost_cal()