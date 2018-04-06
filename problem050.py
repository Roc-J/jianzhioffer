#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        d = dict()
        flag = False
        for item in numbers:
            if item not in d:
                d[item] = 1
            else:
                duplication[0] = item
                flag = True
                break
        return flag