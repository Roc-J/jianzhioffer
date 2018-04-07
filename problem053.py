#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if not s:
            return True
        flag = 1
        for i in range(len(s)):
            if '0' <= s[i] <= '9' or (i == 0 and s[i] in ['+', '-']):
                continue
            elif s[i] == '.' and flag == 1:
                flag += 1
                continue
            elif s[i] in ['e', 'E'] and i < len(s)-1:
                flag += 1
                continue
            elif s[i] in ['+', '-'] and s[i-1] in ['e', 'E']:
                continue
            else:
                return False
        return True

if __name__ == '__main__':
    print(Solution().isNumeric("12e+5.4"))