#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def treeSame(self, left, right):
        if left is None:
            return (right is None)
        if right is None:
            return False
        if left.val != right.val:
            return False
        return self.treeSame(left.left, right.right) and self.treeSame(left.right, right.left)

    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        else:
            return self.treeSame(pRoot.left, pRoot.right)