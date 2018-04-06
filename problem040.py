#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if not array:
            return None

        d = dict()
        for item in array:
            if item not in d:
                d[item] = 1
            else:
                d.pop(item)
        result = d.keys()
        return result