#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

'''
整数中1出现的次数

'''
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        ones = 0
        i = 1
        while i <= n:
            a = n/i
            b = n % i
            ones += (a+8)/10*i + (a % 10 == 1)*(b+1)
            i *= 10

        return ones

if __name__ == '__main__':
    print(Solution().NumberOf1Between1AndN_Solution(11))