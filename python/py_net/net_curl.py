#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request


def curl_test(path):
    with request.urlopen(path) as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', data.decode('utf-8'))

def curl_get_test(path):
    req = request.Request(path)
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(req) as f:
        print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

    

#main
if __name__ == '__main__':
    curl_test('https://www.baidu.com')
    print("[------gut curl-----]")
    curl_get_test('https://www.baidu.com')