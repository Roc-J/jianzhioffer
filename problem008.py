#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

'''
前提是一次只能跳1阶或者2阶的跳法
a.如果两种跳法，一阶或者两阶，那么假定第一次跳的是一阶，那么剩下的就是n-1阶，跳法是f(n-1）
b.假定第一次跳的是2阶，那么剩下的是n-2阶，跳法是f(n-2)
c.由a and b假设可以得出总跳法f(n)=f(n-1)+f(n-2)
d f(1) = 1 f(2)=2
'''
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <= 0:
            return 0
        f1, f2 = 1, 2
        if number == 1:
            return f1
        if number == 2:
            return f2
        for i in range(3, number):
            f = f1+f2
            f1 = f2
            f2 = f
        return f1 + f2


