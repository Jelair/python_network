# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     search2
   Description :
   Author :       simplefly
   date：          2018/1/23
-------------------------------------------------
   Change Activity:
                   2018/1/23:
-------------------------------------------------
"""
__author__ = 'simplefly'

# 从谷歌地理编码API获取一个JSON文档

import requests

def geocode(address):
    parameters = {
        'address' : address,
        'sensor' : 'false'
    }
    base = 'http://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(base, params=parameters)
    answer = response.json()
    print(answer['results'][0]['geometry']['location'])

if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')