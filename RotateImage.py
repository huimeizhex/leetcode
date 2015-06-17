#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def rotate(self, matrix):
        self.my_rotate(matrix, 0, 0, len(matrix))

    def rotate_vertical(self, matrix, x, y, n):
        for i in xrange(0, n):
            matrix[i+x][n+y], matrix[n+x][2*n-i+y] = matrix[n+x][2*n-i+y], matrix[i+x][n+y]
            matrix[i+x][n+y], matrix[n+x][i+y] = matrix[n+x][i+y], matrix[i+x][n+y]
            matrix[n+x][i+y], matrix[2*n-i+x][n+y] = matrix[2*n-i+x][n+y], matrix[n+x][i+y]

    def rotate_matrix(self, matrix, x, y, n, m):
        for i in xrange(0, m):
            for j in xrange(0, m):
                matrix[x+i][y+j], matrix[x+i][y+j+n] = matrix[x+i][y+j+n], matrix[x+i][y+j]
                matrix[x+i+n][y+j], matrix[x+i][y+j] = matrix[x+i][y+j], matrix[x+i+n][y+j]
                matrix[x+i+n][y+j], matrix[x+i+n][y+j+n] = matrix[x+i+n][y+j+n], matrix[x+i+n][y+j]



    def my_rotate(self, matrix, x, y, n):
        if n == 1:
            return 
        trans = n/2
        if n%2 == 1:
            self.rotate_vertical(matrix, x, y, n/2)
            trans += 1 
        self.rotate_matrix(matrix, x, y, trans, n/2)
        self.my_rotate(matrix, x+trans, y, n/2)
        self.my_rotate(matrix, x, y+trans, n/2)
        self.my_rotate(matrix, x, y, n/2)
        self.my_rotate(matrix, x+trans, y+trans, n/2)




if __name__ == "__main__":
    num = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    so = Solution()
    so.rotate(num)
    
    print num
