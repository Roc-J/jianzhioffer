#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution:
    def jumpFloorII(self, number):
        # write code here
        return pow(2, number-1)


if __name__ == '__main__':
    print(Solution().jumpFloorII(5))
