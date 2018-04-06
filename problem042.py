#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        left, right = 0, len(array) - 1
        result = []
        while (left < right):
            if array[left] + array[right] == tsum:
                result.append(array[left])
                result.append(array[right])

            elif array[left] + array[right] < tsum:
                left += 1
            else:
                right -= 1

        return result