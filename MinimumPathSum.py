#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def min_path_sum(self, grid):
        n  = len(grid)
        m = len(grid[0])
        for i in xrange(0, n):
            for j in xrange(0, m):
                if j > 0 and i > 0:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                else:
                    if i > 0:
                        grid[i][j] += grid[i-1][j]
                    if j > 0:
                        grid[i][j] += grid[i][j-1]
        return grid[n-1][m-1]
                


if __name__ == "__main__":
    so = Solution()
    num = [[1, 2, 1], [3, 4]]
    print so.min_path_sum(num)

