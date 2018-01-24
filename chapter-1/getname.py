# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     getname
   Description :
   Author :       simplefly
   date：          2018/1/23
-------------------------------------------------
   Change Activity:
                   2018/1/23:
-------------------------------------------------
"""
__author__ = 'simplefly'

# 将主机名转换为IP地址
import socket

if __name__=='__main__':
    hostname = 'www.python.org'
    addr = socket.gethostbyname(hostname)
    print('The IP address of {} is {}'.format(hostname, addr))