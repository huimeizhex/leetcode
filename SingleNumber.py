class Solution(object):
    def SingleNumber(self, A):
        res = 0
        for i in A:
            res = res ^ i
        return res

if __name__ == "__main__":
    so = Solution()
    print so.SingleNumber([12, 123, 123, 33, 33])
