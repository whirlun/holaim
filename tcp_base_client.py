# -*- coding: utf-8 -*-

import socket

def process_normal_message(msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(('127.0.0.1',21584))

    s.send(msg)
    res = s.recv(2048)

    #s.send('exit')
    s.close()

    return res