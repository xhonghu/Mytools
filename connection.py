import requests
import sys
import time

'''
http://192.168.8.1:801/eportal/?c=Portal&a=login&callback=dr1003&login_method=1&
user_account=%2C0%2C2112012089&user_password=isaac1755&
wlan_user_ip=10.81.63.253&wlan_user_ipv6=&wlan_user_mac=000000000000&
wlan_ac_ip=192.168.8.10&wlan_ac_name=ME60&jsVersion=3.3.3&v=7477

c: Portal
a: login
callback: dr1003
login_method: 1
user_account: ,0,2112012089
user_password: isaac1755
wlan_user_ip: 10.81.63.253
wlan_user_ipv6: 
wlan_user_mac: 000000000000
wlan_ac_ip: 
wlan_ac_name: 
jsVersion: 3.3.3
v: 9749
'''


url = 'http://192.168.8.1:801/eportal/'
data = {
    "c": 'Portal',
    "a": 'login',
    "callback": 'dr1003',
    "login_method": '1',
    "user_account": '221122120304',
    "user_password": '121546Hhx!!!',
    ##在这里修改成服务器的所在的ip地址
    "wlan_user_ip": '10.12.54.224',
    "wlan_user_ipv6": '',
    "wlan_user_mac": '000000000000',
    "wlan_ac_ip": '',
    "wlan_ac_name": '',
    "jsVersion": '3.3.3',
    "v": '9749'
}

header = {
    "Accept": '*/*',
    "Accept-Encoding": 'gzip, deflate',
    "Accept-Language": 'zh-CN,zh;q=0.9',
    "Connection": 'keep-alive',
    "Cookie": 'PHPSESSID=5lr52bqd6t6fns9ng439f0n3e7',
    "Host": '192.168.8.1:801',
    "Referer": 'http://192.168.8.1/',
    "User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0'
}

response = requests.get(url,data,headers=header)
print(f"Response:{response}")

time.sleep(5)
response1 = requests.get(url,data,headers=header)
print(f"Response:{response1}")
