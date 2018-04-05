#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        d = dict()
        for item in numbers:
            if item not in d:
                d[item] = 1
            else:
                d[item] += 1

        result = sorted(d.items(), key=lambda item:item[1])
        if result[-1][1] > len(numbers)/2:
            return result[-1][0]
        else:
            return 0

if __name__ == '__main__':
    print(Solution().MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2]))