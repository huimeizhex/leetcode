#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def search(self, A, target):
        self.res = False
        self.target = target
        pos = self.fin_min(A)        
        if A[pos] == target:
            return True
        self.binary_searh(A, 0, pos-1)
        self.binary_searh(A, pos+1, len(A)-1)
        return self.res


    def binary_searh(self, num, left, right):
        if right < left:
            return 
        mid = (left+right)/2 
        if num[mid] == self.target:
            self.res = True
            return
        if num[left] <= num[right]:
            if self.target > num[mid]:
                self.binary_searh(num, mid+1, right)
            else:
                self.binary_searh(num, left, mid-1)
        else:
            if self.target > num[mid]:
                self.binary_searh(num, left, mid-1)
            else:
                self.binary_searh(num, mid+1, right)



    def fin_min(self, num):
        left = 0
        right = len(num) - 1
        while left < right and num[left] == num[right]:
            left += 1
        mid = (left+right)/2
        if num[mid] > num[left] and num[right] > num[mid]:
            return left
        if num[mid] < num[left] and num[right] < num[mid]:
            return right
     
        
        return self.my_find_min(num, left, right, num[left], num[right])

    def my_find_min(self, num, left, right, lnum, rnum):
        if right <= left:
            return left
        
        mid = (left+right)/2

        if lnum >= rnum:
            if num[mid] >= lnum:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if num[mid] >= rnum:
                right = mid - 1
            else:
                left = mid + 1



        pos = self.my_find_min(num, left, right, lnum, rnum)
        if num[mid] < num[pos]:
            return mid
        else:
            return pos
        





if __name__ == '__main__':
    so = Solution()
    num = [5, 4, 3, 2, 1] 
    num1 = [4, 5, 6, 7, 8, 1, 2, 3]
    num2 = [1,2,3,0,1,1]
    num3 = [10,10,10,-10,-10,-10,-10,-9,-9,-9,-9,-9,-9,-9,-8,-8,-8,-8,-8,-8,-8,-8,-7,-7,-7,-7,-6,-6,-6,-5,-5,-5,-4,-4,-4,-4,-3,-3,-2,-2,-2,-2,-2,-2,-2,-2,-1,-1,-1,-1,-1,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,2,2,2,3,3,3,4,4,4,5,5,5,5,6,6,6,7,7,7,7,7,8,8,8,8,9,9,9,9,9,9,9,10,10]
    num4 = [1,2,2,2,8,1,1]

    print so.search(num3, 8)
