#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1

        root = ListNode(1)
        p = root

        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                root.next = pHead1
                pHead1 = pHead1.next
            else:
                root.next = pHead2
                pHead2 = pHead2.next
            root = root.next
        while pHead1:
            root.next = pHead1
            root = root.next
            pHead1 = pHead1.next
        while pHead2:
            root.next = pHead2
            root = root.next
            pHead2 = pHead2.next

        return p.next