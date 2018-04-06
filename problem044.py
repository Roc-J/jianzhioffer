#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution:
    def ReverseSentence(self, s):
        # write code here
        if s.strip() == "":
            return s
        result = s.split()
        str = ''
        for item in result[::-1]:
            str += " " + item
        return str.lstrip()

if __name__ == '__main__':
    print(Solution().ReverseSentence(""))

