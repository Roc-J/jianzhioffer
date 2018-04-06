#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution:
    def multiply(self, A):
        # write code here
        A1 = [1]
        A2 = [1]
        B = []

        ans = 1
        for item in A:
            ans *= item
            A1.append(ans)
        A1.pop()

        ans = 1
        for item in A[::-1]:
            ans *= item
            A2.append(ans)
        A2.pop()

        for i in range(len(A)):
            B.append(A1[i]*A2[-(i+1)])
        return B

if __name__ == '__main__':
    print(Solution().multiply([1,2,3,4,5]))



