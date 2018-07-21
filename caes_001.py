#!/usr/bin/python
# Author: youyooyou@126.com
# -*- coding: utf-8 -*-
# @Time     : 2018/6/10 17:12
# @Author   : youyooyou@126.com
# @File     : caes_001.py
# @Software : PyCharm
# @ModifyLog:


'''
    题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''


def isnotequal(num_a, num_b, num_c):
    if (num_a != num_b) and (num_a != num_c) and (num_b != num_c):
        return True
    else:
        return False


total_num = 0


for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if isnotequal(i, j, k):
                print(i.__str__() + j.__str__() + k.__str__())
                total_num += 1
print("总共有：" + total_num.__str__() + "个数字。")