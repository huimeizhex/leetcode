#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def unique_paths(self, n, m):
        return self.combination(n+m-2, n-1)
    

    def combination(self, n, m):
        if m == 0 or m == n:
            return 1
        top = 1
        end = 1
        for i in range(1, m+1):
            top = top * (n-i+1)
            end = end * i
        return top/end

if __name__ == "__main__":
    so = Solution()
    print so.unique_paths(3, 3)

