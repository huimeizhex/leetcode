#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def sort_colors(self, A):
        st = -1
        ed = len(A)
        i = 0
        while i < ed:
            if A[i] == 0:
                st += 1 
                A[i], A[st] = A[st], A[i]
                i = max(st+1, i)
                continue
            if A[i] == 1:
                i += 1
                continue
            if A[i] == 2:
                ed -= 1
                A[i], A[ed] = A[ed], A[i]
                continue

if __name__ == '__main__':
    A = [1, 0, 0, 0]
    so = Solution()
    so.sort_colors(A)
    print A
