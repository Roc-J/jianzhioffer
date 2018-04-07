#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        if pNode.right:
            l = pNode.right
            while l.left:
                l = l.left
            return l
        while pNode.next:
            temp = pNode.next
            if temp.left == pNode:
                return temp
            pNode = temp
