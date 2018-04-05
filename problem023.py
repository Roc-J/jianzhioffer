#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False

        root = sequence[-1]

        # 寻找二叉树小于根节点的数
        i = 0
        for item in sequence[:-1]:
            if item > root:
                break
            i += 1

        for item in sequence[i:-1]:
            if item < root:
                return False

        left = True
        if i > 1:
            left = self.VerifySquenceOfBST(sequence[:i])

        right = True
        if i < len(sequence) - 2 and left:
            right = self.VerifySquenceOfBST(sequence[i:-1])

        return left and right