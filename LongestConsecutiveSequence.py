#!/usr/bin/env python
# coding=utf-8
class solution(object):
    def longest_consecutive(self, num):
        pos = {}
        res = 0
        npos = []
        for i in xrange(0, len(num)):
            if num[i] not in npos:
                pos[num[i]] = 1
                res = max(res, 1)
                npos.append(num[i])
            else:
                continue
            if num[i] - 1 in pos:
                pos[num[i]] += pos[num[i]-1] 
                pos[num[i]-pos[num[i]]+1] = pos[num[i]]
                res = max(res, pos[num[i]])
                if pos[num[i]] > 2:
                    del pos[num[i] - 1]
            if num[i] + 1 in pos:
                mid = pos[num[i]+1]
                pos[num[i]+mid] += pos[num[i]]
                res = max(res, pos[num[i]+mid])
                mid1 =  num[i] + mid - pos[num[i]+mid] + 1
                if mid > 1:
                    del pos[num[i]+1]
                pos[mid1] = pos[num[i]+mid]
                if mid1 < num[i]:
                    del pos[num[i]]
        return res      


if __name__ == '__main__':
    so = solution()
    num = [0,3,7,2,5,8,4,6,0,1]
    res = so.longest_consecutive(num)
    print res
