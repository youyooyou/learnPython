#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     : 2018/7/21 13:53
# @Author   : youyooyou@126.com
# @File     : case_004.py
# @Software : PyCharm
# @ModifyLog:


def _test():
    '''
    # 题目：输入某年某月某日，判断这一天是这一年的第几天？
    # 分析：
    1.瑞年
    (1)该年能被4整除，但是不能被100整除
    (2)该年能被400整除
    2.月份
    普通年：
    notLeapYear = {
                    1:31,
                    2:28,
                    3:31,
                    4:30,
                    5:31,
                    6:30,
                    7:31,
                    8:31,
                    9:30,
                    10:31,
                    11:30,
                    12:31
            }
    瑞年：
    LeapYear = {
                    1:31,
                    2:29,
                    3:31,
                    4:30,
                    5:31,
                    6:30,
                    7:31,
                    8:31,
                    9:30,
                    10:31,
                    11:30,
                    12:31
            }
    '''

    notLeapYear = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    LeapYear = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    def isLeapYear(year):
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return True
        else:
            return False

    def calcDate(year, month, date):
        year = int(year)
        month = int(month)
        date = int(date)
        sumDate = date
        if isLeapYear(year):
            for i in range(1, month + 1):
                sumDate += LeapYear[month]
        else:
            for i in range(1, month + 1):
                sumDate += notLeapYear[month]
        print('Today is %s date of %s year.' % (sumDate, year))

    def isLegal(year, month, date):
        year = int(year)
        month = int(month)
        date = int(date)
        if isLeapYear(year):
            if year > 0 and month > 0 and month <= 12 and date > 0 and date <= LeapYear[month]:
                return True
            else:
                return False
        else:
            if year > 0 and month > 0 and month <= 12 and date > 0 and date <= notLeapYear[month]:
                return True
            else:
                return False

    year = input('Input year:')
    month = input('Input month:')
    date = input('Input date:')
    if isLegal(year, month, date):
        calcDate(year, month, date)
    else:
        print('Input is not legal.')


if __name__ == '__main__':
    _test()