#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 0:
            return 0
        res = [1, 2]
        if number == 1:
            return 1
        if number == 2:
            return 2
        for i in range(2, number):
            res.append(res[-1] + res[-2])
        return res[-1]

if __name__ == '__main__':
    print(Solution().rectCover(1))