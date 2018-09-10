# -*-  coding = utf-8 -*- 
"""
根据 ZoomEye 编写的API
"""
import requests
import json

def login(user, passwd):
    data_info = {'username' : user, 'password' : passwd}
    data_encoded = json.dumps(data_info)
    respond = requests.post(url = 'https://api.zoomeye.org/user/login', data = data_encoded)
    #print(respond.text)
    try:
        r_decoded = json.loads(respond.text)
        access_token = r_decoded['access_token']
    except KeyError:
        return '[-] INFO: username or password is wrong, please try again'
    return access_token

def search(queryType, queryStr, pageCount, access_token):
    headers = {'Authorization' : 'JWT ' + str(access_token)}
    print('[-] result: ')
    for i in range(1, int(pageCount)):
        r = requests.get(url = 'https://api.zoomeye.org/' + queryType + '/search?query=' + queryStr + '&page='+str(i),
                        headers = headers)
        response = json.loads(r.text)
        try:
            if queryType == 'host':
                for h in response['matches']:
                    print(h['ip'])
            if queryType == 'web':
                for w in response['matches']:
                    print(w['ip'][0])
        except KeyError:
            print('[ERROR] no hosts found')

def main():
    print(" _____                     _____           ____  ")               
    print("|__  /___   ___  _ __ ___ | ____|   _  ___/ ___|  ___ __ _ _ __") 
    print("  / // _ \ / _ \| '_ ` _ \|  _|| | | |/ _ \___ \ / __/ _` | '_ \ ")
    print(" / /| (_) | (_) | | | | | | |__| |_| |  __/___) | (_| (_| | | | |")
    print("/____\___/ \___/|_| |_| |_|_____\__, |\___|____/ \___\__,_|_| |_|")
    print("                                |___/                            ")
    user = input('[-] Please input your username: ')
    passwd = input('[-] Please input your password: ')
    pageCount = input('[-] Please input your search_page_count: ')
    queryType = input('[-] Please input your search_Type(eg: web/host): ')
    queryStr = input('[-] Please input your search keyword(eg: tomcat): ')
    access_token = login(user, passwd)
    search(queryType, queryStr, pageCount, access_token)

if __name__ == '__main__':
    main()