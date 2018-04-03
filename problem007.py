#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution:
    def Fibonacci(self, n):
        # write code here
        if n<=0:
            return 0
        if n == 1 or n == 2:
            return 1
        else:
            temp1 = 1
            temp2 = 1
            for i in range(3, n):
                temp = temp1 + temp2
                temp1 = temp2
                temp2 = temp
            return temp1+temp2

if __name__ == '__main__':
    for i in range(10):
        print(Solution().Fibonacci(i))