#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/21 11:49
# @Author   : youyooyou@126.com
# @File     : case_003.py
# @Software : PyCharm
# @ModifyLog:

'''
#   题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
'''
'''
分析：
x + 100 = m^2
x + 168 = n^2
n^2 - m^2 = 68
(n + m) * (n - m) = 68
n > m 
'''

def _test():
    IsFound = False
    for m in range(1,67):
        for n in range(m, 68):
            if (n + m) * (n - m) == 68:
                print("该数为:" + str(n * n - 168))
                print('n为%s,m为%s' % (n, m))
                IsFound = True
                break
        if IsFound:
            break
if __name__ == '__main__':
    _test()