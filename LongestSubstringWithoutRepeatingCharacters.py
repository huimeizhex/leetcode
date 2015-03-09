class solution:
    def lengthOfLongestSubstring(self,s):
        pos = {}
        ans = 0
        preans = -1
        for i in xrange(len(s)):
            if s[i] in pos:
                preans = max(preans, pos[s[i]])
                ans = max(ans, i - preans)
                pos[s[i]] = i
            else:
                pos[s[i]] = i
                ans = max(ans, i - preans)
        return ans

if __name__ == '__main__':
    so = solution()
    str1 = raw_input()
    res = so.lengthOfLongestSubstring(str1)
    print res
