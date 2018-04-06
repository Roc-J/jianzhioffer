#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

'''
运用位运算
1. 两个数异或 每一位相加,没有进位
2. 两个数相与,并左移一位,进位
3. 相加

'''
class Solution:
    def Add(self, num1, num2):
        # write code here
        if not num1:
            return num2
        if not num2:
            return num1
        while num2!=0:
            sum = (num1^num2) & 0xFFFFFFFF
            carry = (num1 & num2) <<1
            num1 = sum
            num2 = carry
        return num1 if num1 >> 31 == 0 else num1 - 4294967296

if __name__ =='__main__':
    print(Solution().Add(18,6))