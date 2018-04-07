#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution:
    def __init__(self):
        self.a = []

    def Insert(self, num):
        # write code here
        self.a.append(num)

    def GetMedian(self):
        # write code here
        self.a.sort()
        if len(self.a)%2 == 1:
            return self.a[len(self.a)/2]
        else:
            return (self.a[len(self.a)/2-1] + self.a[len(self.a)/2])/2.0