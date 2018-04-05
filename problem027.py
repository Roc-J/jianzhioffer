#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

'''
字符串的排列
按字典序是指不同排列的先后关系是从左到右逐个比较对应的数字的先后来决定，比如'ab','ba'来排序
先比较最左边的字母，'a'比'b'靠前，所以'ab'排在'ba'前面。使用sorted函数可以达到这个效果

'''

class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        if len(ss) == 1:
            return ss
        L = []
        a = list(ss)
        # 每次取出字符串中的每一个字符放在组合字符串的最前面
        for i in ss:
            b = a[:]
            # 原始字符串除去已拿出字符后的字符串
            b.remove(i)
            # 遍历下一次迭代返回的一个排列
            for li in self.Permutation("".join(b)):
                L.append(''.join([i, li]))

        return sorted(list(set(L)))

if __name__ == '__main__':
    print(Solution().Permutation('abcd'))