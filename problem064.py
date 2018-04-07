#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not num or size==0 or size>len(num):
            return []
        queue = []
        for i in range(size):
            queue.append(num.pop(0))
        result = []
        result.append(max(queue))
        while num:
            queue.append(num.pop(0))
            queue.pop(0)
            result.append(max(queue))
        return result