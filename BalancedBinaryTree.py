#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def is_balanced(self, root):
        self.res = True
        if root is None:
            return self.res
        deep1 = self.my_is_balanced(root.left, 1)
        deep2 = self.my_is_balanced(root.right, 1)
        if abs(deep2 - deep1) > 1:
            self.res = False
        return self.res

    def my_is_balanced(self, node, deep):
        if node is None:
            return deep
        deep1 = self.my_is_balanced(node.left, deep+1)
        deep2 = self.my_is_balanced(node.right, deep+1)
        if abs(deep1 - deep2) > 1:
            self.res = False
        return max(deep1, deep2)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

if __name__ == "__main__":
    head = TreeNode(4)
    head.right = TreeNode(3)
    head.right.right = TreeNode(2)
    so = Solution()
    print so.is_balanced(head)
