#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket, time, threading

# 服务端接收处理数据
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        #time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

# 服务端
def tcp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9999))
    s.listen(5)
    print('Waiting for connection...')
    while True:
        # 接受一个新连接:
        sock, addr = s.accept()
        # 创建新线程来处理 TCP 连接:
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()

# 客户端
def tcp_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接:
    s.connect(('127.0.0.1', 9999))
    # 接收欢迎消息:
    print(s.recv(1024).decode('utf-8'))
    for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
        s.send(data)
    print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()

#main
if __name__ == '__main__':
    tcp_server()
    tcp_client()