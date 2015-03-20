#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def __init__(self):
        self.res = []

    def post_order_traversal(self, root):
        if root is None:
            return None
        self.post_order_traversal(root.left)
        self.post_order_traversal(root.right)
        self.res.append(root.val)
        return self.res
