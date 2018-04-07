#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        nodeStack = [pRoot]
        result = []
        while nodeStack:
            res = []
            nextStack = []
            for node in nodeStack:
                res.append(node.val)
                if node.left:
                    nextStack.append(node.left)
                if node.right:
                    nextStack.append(node.right)
            nodeStack = nextStack
            result.append(res)
        returnResult = []
        for i, v in enumerate(result):
            if i%2 == 0:
                returnResult.append(v)
            else:
                returnResult.append(v[::-1])
        return returnResult