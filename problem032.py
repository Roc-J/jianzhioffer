#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

'''
把数组排成最小的数

'''
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return 0
        numbers = list(map(str, numbers))
        numbers.sort(cmp=lambda x, y: cmp(x+y, y+x))
        return "".join(numbers).lstrip('0') or '0'

if __name__ == '__main__':
    print(Solution().PrintMinNumber([3,32,321]))