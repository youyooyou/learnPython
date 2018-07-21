#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/21 18:01
# @Author   : youyooyou@126.com
# @File     : case_005.py
# @Software : PyCharm
# @ModifyLog:


def _test():
    '''
    # 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
    :return:
    '''
    x = int(input('Input x:'))
    y = int(input('Input y:'))
    z = int(input('Input z:'))
    numMax = max(x, y, z)
    numMin = min(x, y, z)
    isMaxFound = False
    isMinFound = False
    for i in (x, y, z):
        if i == numMax and not isMaxFound:
            isMaxFound = True
            continue
        if i == numMin and not isMinFound:
            isMinFound = True
            continue
        print(numMax, i, numMin)
        break


if __name__ == '__main__':
    _test()