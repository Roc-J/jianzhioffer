#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution:
    def getLower(self, data, k):
        start, end = 0, len(data)-1
        mid = (start + end) /2
        while start<=end:
            if data[mid] < k:
                start = mid + 1
            else:
                end = mid - 1
            mid = (start + end)/2
        return start

    def getUpper(self, data, k):
        start, end = 0, len(data) - 1
        mid = (start + end) / 2
        while start <= end:
            if data[mid] <= k:
                start = mid + 1
            else:
                end = mid - 1
            mid = (start + end) / 2
        return end

    def GetNumberOfK(self, data, k):
        # write code here
        lower = self.getLower(data, k)
        upper = self.getUpper(data, k)

        return upper - lower + 1