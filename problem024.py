#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

'''
递归先序遍历树，把节点加入到路径
若该节点是叶子节点则比较当前路径是否等于期待和
弹出节点，每一轮递归返回到父节点，当前路径也应该回退一个节点

'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []

        result = []

        # 找路径的函数
        def FindPathMain(root, path, currentSum):
            currentSum += root.val

            path.append(root)
            # 判断是不是叶子节点
            isLeaf = root.left == None and root.right == None

            if currentSum == expectNumber and isLeaf:
                onePath = []
                for node in path:
                    onePath.append(node.val)
                result.append(onePath)

            if currentSum < expectNumber:
                if root.left:
                    FindPathMain(root.left, path, currentSum)
                if root.right:
                    FindPathMain(root.right, path, currentSum)

            path.pop()

        FindPathMain(root, [], 0)

        return result
