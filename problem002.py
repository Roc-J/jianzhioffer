#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        items = s.split(" ")
        result = ""
        for item in items:
            result += item+"%20"
        return result[:-3]