#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

# class Solution:
#     # s, pattern都是字符串
#     def match(self, s, pattern):
#         # write code here
#         # pattern 字符串长度为0
#         if len(pattern) == 0 and len(s) == 0:
#             return True
#         # pattern 字符串长度为1
#         elif len(pattern) == 1:
#             if len(s) == 1 and (s[0] == pattern or pattern == '.'):
#                 return True
#             else:
#                 return False
#         # pattern字符串长度大于2
#         elif len(pattern) > 2:
#             if pattern[1] == '*':
#                 if pattern[0] == '.':
#                     ptnum = len(s)
#                 elif s == '' or s[0] != pattern[0]:
#                     ptnum = 0
#                 else:
#                     ptnum = 1
#                     idx = 1
#                     while idx < len(s):
#                         if s[idx] == s[0]:
#                             ptnum += 1
#                             idx += 1
#                         else:
#                             break
#                 for i in range(ptnum+1):
#                     if self.match(s[i:], pattern[2:]):
#                         return True
#                 return False
#             else:
#                 if s[0] == pattern[0] or pattern[0] == '.':
#                     return self.match(s[1:], pattern[1:])
#                 else:
#                     return False
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        if len(s) == 0 and len(pattern) == 0:
            return True
        if len(s) > 0 and len(pattern) == 0:
            return False
        if len(pattern) > 1 and pattern[1] == '*':
            if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
                return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)
            else:
                return self.match(s, pattern[2:])
        if (len(s) > 0 and (pattern[0] == '.' or pattern[0] == s[0])):
            return self.match(s[1:], pattern[1:])
        return False

if __name__ == '__main__':
    print(Solution().match("", "."))