#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        if abs(self.maxDepth(pRoot.left) - self.maxDepth(pRoot.right)) >1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def maxDepth(self,root):
        if not root:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1