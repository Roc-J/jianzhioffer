#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None

        self.arr = []
        self.midTravel(pRootOfTree)
        for i, v in enumerate(self.arr[:-1]):
            v.right = self.arr[i+1]
            self.arr[i+1].left = v
        return self.arr[0]


    def midTravel(self, root):
        if not root:
            return
        self.midTravel(root.left)
        self.arr.append(root)
        self.midTravel(root.right)