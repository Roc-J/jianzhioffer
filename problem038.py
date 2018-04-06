#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        l = self.TreeDepth(pRoot.left)
        r = self.TreeDepth(pRoot.right)
        return max(l,r) + 1
        # queue = []
        # queue.append(pRoot)
        # level = 0
        # while len(queue)>0:
        #     len1 = len(queue)
        #     while len1:
        #         node = queue.pop(0)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #         len1 -=1
        #     level += 1
        # return level