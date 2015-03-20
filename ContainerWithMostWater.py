#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def max_area(self, height):
        if len(height) == 0:
            return 0
        pos = []
        for i in xrange(0, len(height)):
            pos.append((i, height[i]))
        pos = sorted(pos, key = lambda value: value[1], reverse=True)
        
        res = 0
        max_pos = min_pos = pos[0][0]
        for i in xrange(1, len(pos)):
            max_pos = max(max_pos, pos[i][0])
            min_pos = min(min_pos, pos[i][0])
            res = max(res, (max_pos - min_pos)*pos[i][1])
        return res
        
            



if __name__ == "__main__":
    num = [1, 2, 3, 4, 5]
    so = Solution()
    print so.max_area([])



