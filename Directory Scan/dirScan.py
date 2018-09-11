# -*- coding:utf-8 -*-

import requests
from threading import Thread, activeCount
import  queue


def dir_scan(url):
    """
    扫描url
    """
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://www.baidu.com'
    }
    status_code = [200]
    
    try:
        req = requests.head(url.strip(), timeout = 8, headers = headers)
        if req.status_code in status_code:
            print('status_code: %s url: %s'%(req.status_code, url.strip('\n')))
            open('exist_url.txt','a').write(url)
    except:
        print('no url')

def open_pathfile(url, file):
    scan_queue = queue.Queue()
    path = open(file, 'r').readlines()
    for line in path:
        if url.endswith('/'):
            if line.startswith('/'):
                scan_queue.put(url + line[1:])
            else:
                scan_queue.put(url + line)
        else:
            if line.startswith('/'):
                scan_queue.put(url + line)
            else:
                scan_queue.put(url + '/' + line)
    return scan_queue

def check_url(url):
    if url.startswith('http://') or url.startswith('https://'):
        pass
    else:
        url = 'http://'+ url
    return url

def main():
    print('''
    ____  _      ____                  
    |  _ \(_)_ __/ ___|  ___ __ _ _ __  
    | | | | | '__\___ \ / __/ _` | '_ \ 
    | |_| | | |   ___) | (_| (_| | | | |
    |____/|_|_|  |____/ \___\__,_|_| |_|
    
    ''')
    url = input('[*] Please input your target url: ')
    thread_num = input('[*] Please input your threadnum: ')
    pathfile = input('[*] Please input your dictionary: ')
    _url = check_url(url)
    print('The number of threads is %s '% thread_num)
    print('[*] scanning...') 
    scan_queue = open_pathfile(url, pathfile)
    while scan_queue.qsize() > 0:
        if activeCount() <= int(thread_num):
            Thread(target=dir_scan, args=(scan_queue.get(),)).start()

            
if __name__ == '__main__':
    main()