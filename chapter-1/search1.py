# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     search1
   Description :
   Author :       simplefly
   date：          2018/1/23
-------------------------------------------------
   Change Activity:
                   2018/1/23:
-------------------------------------------------
"""
__author__ = 'simplefly'

# 获取经度和纬度

from pygeocoder import Geocoder

if __name__ == '__main__':
    address = '207 N. Defiance St, Archbold, OH'
    print(Geocoder.geocode(address)[0].coordinates)