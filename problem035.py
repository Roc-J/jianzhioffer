#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk
'''

python不通过
'''
class Solution:
    def InversePairs(self, data):
        # write code here
        count = 0
        copy = []
        for i in data:
            copy.append(i)
        copy.sort()

        for i in range(len(copy)):
            count += data.index(copy[i])
            count %= 1000000007
            data.remove(copy[i])

        return count