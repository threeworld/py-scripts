# -*- coding = utf-8 -*-

import requests
import json
 
def what_cms(url):
        headers = {
                'Connection': 'keep-alive',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'DNT': '1',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
                    }
        post={
                'hash':'0eca8914342fc63f5a2ef5246b7a3b14_7289fd8cf7f420f594ac165e475f1479',
                'url':url,
        }
        r=requests.post(url='http://whatweb.bugscaner.com/what/', data=post, headers=headers)
        dic=json.loads(r.text)
        if dic['cms']=='':
                print('Sorry,Unidentified........')
        else:
                print('CMS:' + dic['cms'])
if __name__ == '__main__':
        url=input('PLEASE INPUT YOUR TARGET:')
        what_cms(url)