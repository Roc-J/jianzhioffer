#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    # 使用递归的方法
    # def Clone(self, pHead):
    #     # write code here
    #     if not pHead:
    #         return None
    #
    #     newNode = RandomListNode(pHead.label)
    #     newNode.random = pHead.random
    #     newNode.next = self.Clone(pHead.next)
    #     return newNode

    # 使用三步
    # 1. 把复制的结点链接链接在原始链表的每一对应结点后面
    # 2. 把复制的结点的random指针指向被复制结点的random的下一个结点
    # 3. 拆分成两个链表，奇数位置为原链表，偶数位置为复制链表，注意复制链表的最后一个结点的next指针不能跟原链表指向同一个空结点，next指针要重新赋值None

    def Clone(self, pHead):
        if not pHead:
            return None

        root = pHead

        # 第一步
        while root:
            rootnext = root.next
            copynode = RandomListNode(root.label)
            copynode.next = rootnext
            root.next = copynode
            root = rootnext

        root = pHead

        # 第二步
        while root:
            rootrandom = root.random
            copynode = root.next
            if rootrandom:
                copynode.random = rootrandom.next
            root = copynode.next

        # 第三步
        root = pHead
        copynode = pHead.next
        while root:
            copynode = root.next
            rootnext = copynode.next
            root.next = rootnext

            if rootnext:
                copynode.next = rootnext.next
            else:
                copynode.next = None
            root = rootnext

        return copynode