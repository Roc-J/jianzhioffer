#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution:
    def StrToInt(self, s):
        # write code here
        s = s.strip()
        newStr = []
        for i in range(len(s)):
            if '0' <= s[i] <= '9' or (s[i] in ['+','-'] and i==0):
                newStr.append(s[i])
            else:
                return 0
                break
        if newStr in ([],['+'],['-']):
            return 0
        elif -2147483648 <= int(''.join(newStr)) <= 2147483647:
            return int(''.join(newStr))
        elif int(''.join(newStr)) > 2147483647:
            return 2147483647
        else:
            return -2147483648