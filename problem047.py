#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution:
    def Sum_Solution(self, n):
        # write code here
        ans = n
        return ans and self.Sum_Solution(n-1)+n
