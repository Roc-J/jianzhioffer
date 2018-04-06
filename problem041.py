#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk
'''
和为S的连续正数序列
'''
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here

        # res = []
        # for i in range(1, tsum // 2 + 1):
        #     sumRes = i
        #     for j in range(i + 1, tsum // 2 + 2):
        #         sumRes += j
        #         if sumRes == tsum:
        #             res.append(list(range(i, j + 1)))
        #             break
        #         elif sumRes > tsum:
        #             break
        # return res
        res = []
        q = []
        start, end = 1,2
        mid = (1+tsum)/2
        qsum = start + end
        if tsum < 3:
            return res
        while start < mid and end < tsum:
            while qsum > tsum:
                qsum = qsum - start
                start += 1
            if qsum == tsum:
                res.append(range(start, end+1))
            end += 1
            qsum += end
        return res

if __name__ == '__main__':
    print(Solution().FindContinuousSequence(100))

