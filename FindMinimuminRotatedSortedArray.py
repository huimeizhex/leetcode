#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def fin_min(self, num):
        left = 0
        right = len(num) - 1
        mid = (left+right)/2
        if num[mid] >= num[left] and num[right] >= num[mid]:
            return num[left]
        if num[mid] <= num[left] and num[right] <= num[mid]:
            return num[right]
            
        return self.my_find_min(num, left, right, num[left], num[right])

    def my_find_min(self, num, left, right, lnum, rnum):
        if right <= left:
            return num[left]
        
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
        return min(num[mid], self.my_find_min(num, left, right, lnum, rnum))
        





if __name__ == '__main__':
    so = Solution()
    num = [5, 4, 3, 2, 1] 
    print so.fin_min(num)
