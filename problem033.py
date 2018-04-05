#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

'''
丑数
'''
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <=0:
            return 0
        res = [1]
        t2, t3, t5 = 0, 0, 0
        nextId = 1
        while nextId < index:
            minNum = min(res[t2]*2, res[t3]*3, res[t5]*5)
            res.append(minNum)
            if minNum == res[t2]*2:
                t2 += 1
            if minNum == res[t3]*3:
                t3 += 1
            if minNum == res[t5]*5:
                t5 += 1
            nextId += 1
        return res[-1]

if __name__ == '__main__':
    print(Solution().GetUglyNumber_Solution(15))
