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
x + 100 + 168 = n^2
n^2 - m^2 = 168
(n + m) * (n - m) = 168
n > m >= 0
n - m 最小值为1
n + m 最大为168
n最大值为168
m最大值为167
'''

def _test():
    for m in range(0, 168):
        for n in range(m + 1, 169):
            #print('n=%s,m=%s' % (n, m))
            if (n + m) * (n - m) == 168:
                print("该数为:" + str(n * n - 168 - 100))
                print("该数为:" + str(m * m - 100))
                print('n为%s,m为%s' % (n, m))
if __name__ == '__main__':
    _test()