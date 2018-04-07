#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        global result
        result = []
        self.inorder(pRoot)
        if k<=0 or k>len(result) or not pRoot:
            return None
        else:
            return result[k-1]

    def inorder(self, root, k):
        if not root:
            return None
        self.inorder(root.left)
        result.append(root)
        self.inorder(root.right)