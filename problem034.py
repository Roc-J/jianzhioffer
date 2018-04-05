#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        d = dict()
        for item in s:
            if item not in d:
                d[item] = 1
            else:
                d[item] += 1

        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1

if __name__ == '__main__':
    print(Solution().FirstNotRepeatingChar('googgle'))