#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution:
    def reOrderArray(self, array):
        # write code here
        jishu = []
        oushu = []
        for i in range(len(array)):
            if array[i] % 2 == 1:
                jishu.append(array[i])
            else:
                oushu.append(array[i])
        return jishu + oushu

if __name__ == '__main__':
    print(Solution().reOrderArray([1,2,3,4,5,6,7,8,9]))