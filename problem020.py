#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, node):
        # write code here
        if not self.minstack:
            self.minstack.append(node)
        else:
            self.minstack.append(min(self.minstack[-1], node))
        self.stack.append(node)

    def pop(self):
        # write code here
        self.minstack.pop()
        if self.stack:
            return self.stack.pop()

    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]

    def min(self):
        # write code here
        if self.minstack:
            return self.minstack[-1]