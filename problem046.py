#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if not m or not n:
            return -1
        numbers = range(n)
        i = 0
        while len(numbers)>1:
            i = (m-1 + i) % len(numbers)
            numbers.pop(i)
        return numbers[-1]

if __name__ == '__main__':
    print(Solution().LastRemaining_Solution(5,2))

