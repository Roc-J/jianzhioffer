#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

'''
连续数组的最大子序列
小于0的舍弃
'''
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return
        s = 0
        result = array[0]
        for item in array:
            s += item
            if result < s:
                result = s
            if s < 0:
                s = 0
        return result

if __name__ == '__main__':
    print(Solution().FindGreatestSumOfSubArray([-2,-8,-1,-5,-9]))