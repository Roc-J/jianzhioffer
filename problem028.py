#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

'''
摩尔投票
'''
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        result = numbers[0]
        times = 1
        for i in range(1, len(numbers)):
            if times == 0:
                result = numbers[i]
                times = 1
            elif numbers[i] == result:
                times += 1
            else:
                times -= 1

        times = 0
        for item in numbers:
            if item == result:
                times += 1

        if times > len(numbers)/2:
            return result
        else:
            return 0

if __name__ == '__main__':
    print(Solution().MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2]))