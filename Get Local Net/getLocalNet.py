# -*- coding: utf-8 -*-

"""
create_time:2018.9.8
"""

import json
import requests
import re

def getLocalNet():
    '''
    获得本地上网的IP相关信息
    :param: None
    :return: None
    '''
    s = requests.session() 
    rexIP = r'\{[\s\S]+\}'
    rexOperator = r'(\s\S*)</b><br/>'

    # 获取本地上网的IP
    ipUrl = 'http://pv.sohu.com/cityjson'
    ipContext = re.findall(rexIP, s.get(ipUrl).content.decode('gbk'))
    ipInfo = ipContext[0]

    #json解析
    dicIP = json.loads(ipInfo)
    
    #获取运营商
    operatorContext = s.get('http://wap.ip138.com/ip.asp?ip=%s'% dicIP['cip']).content.decode('utf-8')
    operator  = re.findall(rexOperator, operatorContext)

    print('您现在上网的IP为：%s %s %s' % (dicIP['cip'], dicIP['cname'], operator[0]))


if __name__ == '__main__':

    getLocalNet()