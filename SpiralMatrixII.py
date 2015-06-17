#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def generate_matrix(self, n):
        self.size = n
        self.res = []
        for i in xrange(0, n):
            self.res.append(n*[0])
        self.my_dfs(1, 0, 0, 'r')
        return self.res

    def my_dfs(self, i, col, row, des):
        if col < 0 or col >= self.size or row < 0 or row >= self.size:
            return

        if self.res[col][row] !=0 or i > self.size**2:
            return 
        self.res[col][row] = i
        if des == 'r':
            if row == self.size -1 or self.res[col][row+1] != 0:
                des = 'd'
                self.my_dfs(i+1, col+1, row, des)
            else:
                self.my_dfs(i+1, col, row+1, des)

        if des == 'd':
            if col == self.size - 1 or self.res[col+1][row] !=0:
                des = 'l'
                self.my_dfs(i+1, col, row-1, des)
            else:
                self.my_dfs(i+1, col+1, row, des)

        if des == 'l':
            if row == 0 or self.res[col][row-1] !=0:
                des = 't'
                self.my_dfs(i+1, col-1, row, des)
            else:
                self.my_dfs(i+1, col, row-1, des)

        if des == 't':
            if col == 0 or self.res[col-1][row] !=0:
                des = 'r'
                self.my_dfs(i+1, col, row+1, des)
            else:
                self.my_dfs(i+1, col-1, row, des)


if __name__ == "__main__":
    so = Solution()
    for i in xrange(0, 6):
        print so.generate_matrix(i)

