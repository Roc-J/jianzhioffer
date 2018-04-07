#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''
        self.d = dict()

    def FirstAppearingOnce(self):
        # write code here
        d = dict()
        for i in self.s:
            if self.d[i] == 1:
                return i
        return '#'

    def Insert(self, char):
        # write code here
        self.s += char
        if char not in self.d:
            self.d[char] = 1
        else:
            self.d[char] += 1
