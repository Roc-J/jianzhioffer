#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        result = []
        if listNode == None:
            return result
        else:
            result.append(listNode.val)
            while listNode.next != None:
                listNode = listNode.next
                result.append(listNode.val)
        return result[::-1]

if __name__ == '__main__':
    print(Solution().printListFromTailToHead())
