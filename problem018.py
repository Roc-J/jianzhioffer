#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:

    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return root
        left = root.left
        root.left = root.right
        root.right = left
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root


