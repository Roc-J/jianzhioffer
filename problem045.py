#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        numbers.sort()
        kings = 0
        diff = 0
        for i in range(len(numbers)-1):
            if numbers[i] == 0:
                kings += 1
                continue
            if numbers[i+1] == numbers[i]:
                return False
            diff += numbers[i+1] - numbers[i] - 1
        if diff <= kings:
            return True
        else:
            return False

if __name__ == '__main__':
    print(Solution().IsContinuous([3,0,0,0,0]))