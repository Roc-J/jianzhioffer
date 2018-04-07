#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return None
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
            result.append(res)
            nodeStack = nextStack
        return result

