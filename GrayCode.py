#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def gray_code(self, n):
        hash = {}
        res = []
        if n == 0:
            return [0]
        hash[0] = 0
        res.append(0)
        for i in xrange(1, 2**n):
            j = 0
            while j < n:
                start = res[-1]
                start = start^(1<<j)
                if start not in hash:
                    hash[start] = 1
                    res.append(start)
                    break
                j += 1
        return res

            





if __name__ == "__main__":
    so = Solution()
    num = raw_input()
    print so.gray_code(int(num))
