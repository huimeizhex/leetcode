#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def permute(self, num):
        self.my_permute(num, len(num))
        return self.res 

    def my_permute(self, num, n):

        if n == 0:
            if len(self.ans):
                mid = []
                mid.extend(self.ans)
                self.res.append(mid)
                #print self.res
                return 
                
        for i in xrange(0, len(num)):
            if i not in self.pos:
                self.pos.append(i)
                self.ans.append(num[i])
                self.my_permute(num, n-1)
                self.pos.pop()
                self.ans.pop()


    def __init__(self):
        self.res = []
        self.pos = []
        self.ans = []

class test(object):
    def __init__(self):
        self.res = []

    def add(self, num):
        self.my_add(num)
        return self.res

    def my_add(self, num):
        self.res.append(num)
        

if __name__ == "__main__":
    so = Solution()
    num = [1, 2, 3]
    num1 = [3, 5, 6]
    num2 = []
    print so.permute(num)
