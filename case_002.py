#!/usr/bin/python
# Author: youyooyou@126.com
# -*- coding: utf-8 -*-
# @Time     : 2018/6/10 17:42
# @Author   : youyooyou@126.com
# @File     : case_002.py
# @Software : PyCharm
# @ModifyLog:

'''
    题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，
    奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分
    按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，
    高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部
    分，可提成3%；60万到100万之间时，高于60万元的部分，可提成
    1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入
    当月利润I，求应发放奖金总数？
    I <= 10         10%     10
    10 < I <= 20    7.5%    10
    20 < I <= 40    5%      20
    40 < I <= 60    3%      20
    60 < I <= 100   1.5%    40
    I < 100         1%      ..
'''


def award_1(I):
    sum_award = 0
    if (I - 10 <= 0):
        sum_award += I * 0.1
    elif (I - 20 <= 0):
        sum_award += (I - 10) * 0.075 + 10 * 0.1
    elif (I - 40 <= 0):
        sum_award += (I - 20) * 0.05 + 10 * 0.1 + 10 * 0.075
    elif (I - 60 <= 0):
        sum_award += (I - 40) * 0.03 + 10 * 0.1 + 10 * 0.075 + 20 * 0.005
    elif (I - 100 <= 0):
        sum_award += (I - 60) * 0.015 + 10 * 0.1 + 10 * 0.075 + 20 * 0.005 + 20 * 0.003
    else:
        sum_award += (I - 100) * 0.001 + 10 * 0.1 + 10 * 0.075 + 20 * 0.005 + 20 * 0.003 + 40 * 0.015
    return sum_award


def award_2(I):
    I_list = [10, 20, 40, 60, 100, 101]
    I_bit = [0.1, 0.075, 0.05, 0.03, 0.015, 0.001]
    for i in range(0, 6):
        if (I_list[i] > I):

            break

i = int(input('净利润(W元):'))
print(award_1(i).__str__() + "W元。")

