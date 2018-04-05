#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

import heapq
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput) or k == 0:
            return []
        heaq = []
        for i in tinput:
            heapq.heappush(heaq, i)
        result = []
        for i in range(k):
            result.append(heapq.heappop(heaq))
        return result

if __name__ == '__main__':
    print(Solution().GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],4))