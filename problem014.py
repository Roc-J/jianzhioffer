#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        # res = []
        # while head:
        #     res.append(head.val)
        #     head = head.next
        # if k>len(res) or k <1:
        #     return
        # return res[-k]

        p = head
        while(k>0):
            if p==None:
                return None
            k-=1
            p = p.next
        while p:
            p = p.next
            head = head.next
        return head