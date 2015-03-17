#!/usr/bin/env python
# coding=utf-8
class Sulotion(object):
    def find_peak_element(self, num):
        return self.my_find_peak_element(num, 0, len(num)-1)

    def my_find_peak_element(self, num, left, right):
        if right <= left:
            return left
        mid = (left+right)/2
        
        if mid == 0 and num[mid] > num[mid+1]:
            return mid
        
        if mid == len(num) - 1 and num[mid] > num[mid-1]:
            return mid
        
        if num[mid] > num[mid-1] and num[mid] > num[mid+1]:
            return mid
        
        if num[mid+1] > num[mid]:
            return self.my_find_peak_element(num, mid+1, right)
        else:
            return self.my_find_peak_element(num, left, mid-1)



if __name__ == "__main__":
    so = Sulotion()
    num = [1, 2, 3, 4, 5, 6, 7, 3, 2, 1]
    num1 = [1, 2, 1]
    print so.find_peak_element(num1)

