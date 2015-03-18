#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def remove_element(self, A, elem):
        while elem in A:
            A.remove(elem)
        return len(A)

if __name__ == "__main__":
    num = [1, 2, 3, 4, 4, 4, 4]
    so = Solution()
    print so.remove_element(num, 4)

