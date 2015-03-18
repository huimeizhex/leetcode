#!/usr/bin/env python
# coding=utf-8
class Solution(object):
        

    def generate_parent_thesis(self, n):
        self.res = []
        self.list = []
        self.map = {}
        self.my_dfs(n, 0, 0)
        return self.res
    
    def convert(self, info):
        ans = list(info)
        c_map = {
            '0':'(',
            '1': ')'
        }
        length = len(info)
        for i in xrange(0, length/2):
            ans[i] = c_map[info[2*i]]
            ans[length-1-i] = c_map[info[2*i+1]]
        return ''.join(ans)
    

    def my_dfs(self, n, b, p, pos=None):
        
        if pos:
            self.list.append(pos)

        if abs(b-p) > 2*n or b<0 or p<0:
            if pos:
                self.list.pop()
            return

        if n == 0:
            info = ''.join(self.list)
            if info not in self.map:
                self.map[info] = 1
                self.res.append(self.convert(info))
            if pos:
                self.list.pop()
            return 
        
        self.my_dfs(n-1, b+1, p+1, '01')
        self.my_dfs(n-1, b+1, p-1, '00')
        self.my_dfs(n-1, b-1, p+1, '11')
        self.my_dfs(n-1, b-1, p-1, '10')
        
        if pos:
            self.list.pop()
        

if __name__ == "__main__":
    so = Solution()
    print so.generate_parent_thesis(3)
