
#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution:
    def reverseStr(self, s, start, end):
        while start < end:
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1

    def LeftRotateString(self, s, n):
        # write code here
        # return s[n:]+s[:n]
        if not s or n < 0:
            return ''
        if n > len(s):
            n = n % len(s)
        s = list(s)
        self.reverseStr(s, 0, n-1)
        self.reverseStr(s, n, len(s)-1)
        self.reverseStr(s, 0, len(s)-1)
        return "".join(s)


if __name__ == '__main__':
    print(Solution().LeftRotateString('abcXYZdef', 3))