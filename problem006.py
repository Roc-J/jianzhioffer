#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        '''
        还是考察二分，旋转数组其实就是两个有序的子数组，

        :param rotateArray:
        :return:
        '''
        # write code here
        if len(rotateArray) == 0:
            return 0
        left, right = 0, len(rotateArray)-1
        while(left < right):
            mid = (left + right)/2
            if rotateArray[mid] < rotateArray[right]:
                right = mid
            elif rotateArray[mid] > rotateArray[right]:
                left = mid + 1
            else:
                right = right - 1
        return rotateArray[left]

if __name__ == '__main__':
    print(Solution().minNumberInRotateArray([3,4,5,1,2]))