#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def sameTree(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False

        return pRoot1.val == pRoot2.val and self.sameTree(pRoot1.left, pRoot2.left) and self.sameTree(pRoot1.right, pRoot2.right)

    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot1 == None or pRoot2 == None:
            return False
        return self.sameTree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)













