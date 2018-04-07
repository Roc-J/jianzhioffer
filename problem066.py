#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution:
    def __init__(self):
        self.visit = {}

    def movingCount(self, threshold, rows, cols):
        # write code here
        return self.moving(threshold, rows, cols, 0, 0)

    def moving(self, threshold, rows, cols, row, col):
        if row >= rows or col >= cols or row < 0 or col < 0:
            return 0
        if (row, col) in self.visit:
            return 0
        if sum(map(int, str(row) + str(col))) > threshold:
            return 0

        self.visit[(row, col)] = 1

        return 1 + self.moving(threshold, rows, cols, row-1, col) + self.moving(threshold, rows, cols, row+1, col) + self.moving(threshold, rows, cols, row, col-1) + self.moving(threshold, rows, cols, row, col+1)