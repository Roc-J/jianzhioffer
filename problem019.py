#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        # 得到行数和列数
        rows = len(matrix)
        cols = len(matrix[0])

        # 判断是否为空 或只有一行，直接输出
        if not matrix or not matrix[0]:
            return matrix

        result = []
        top, left, right, bottom = 0, 0, cols - 1, rows - 1

        # 然后进行打印
        while (top <= bottom and left <= right):
            # 从左到右
            for i in range(left, right + 1):
                result.append(matrix[top][i])

            # 从上到下
            for i in range(top + 1, bottom + 1):
                result.append(matrix[i][right])

            # 从右到左
            for i in range(right - 1, left - 1, -1):
                if bottom > top:
                    result.append(matrix[bottom][i])

            for i in range(bottom - 1, top, -1):
                if right > left:
                    result.append(matrix[i][left])

            top += 1
            left += 1
            right -= 1
            bottom -= 1

        return result