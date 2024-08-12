# -*- coding: utf-8 -*-
import json
import socket
import time
import datetime
import requests

# 手机、邮箱、或用户名
account = f'admin'
# 密码
password = f'cdnfly123'

# 使用了Cdnfly的网站的url
url_website = f'https://demo.cdnfly.cn'

# 你使用ddns的域名
domain = f'test1.haha44444.top'
# 端口
port = f'25565'
# 权重
weight = f'1'

# 更改转发列表中第x行的转发
# 1，2，3，4，按照四层转发的顺序填就好，以此类推，如果你只有一个转发保持默认即可
forward_list_row_x = f'1'


def get_token():
    url = f'{url_website}/login'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    data = {
        "account": account,
        "password": password,
        "code": "",
        "captcha": ""
    }
    session = requests.session()
    res = session.post(url, json=data, headers=headers)
    token = res.json()
    return token['data']['access_token']


def change_ip(ip):
    url_put = f'{url_website}/streams/{forward_list_row_x}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
        'Access-Token': f'{get_token()}'
    }

    data = json.dumps({
        "backend": [
            {
                "index": 0,
                "addr": ip,
                "weight": weight,
                "state": "up"
            }
        ]
    })
    session = requests.session()
    res = session.put(url_put, headers=headers, data=data)
    print(res)


def get_ipAddresses(domain):
    ipAddresses = [0]
    while True:
        time.sleep(2)
        ip = socket.gethostbyname(domain)
        if ip != ipAddresses[-1]:
            ipAddresses.append(ip)
            print(str(datetime.datetime.now())[:19] + '===>' + ip)
            change_ip(ip)


if __name__ == "__main__":
    get_ipAddresses(domain)
