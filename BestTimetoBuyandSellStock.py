#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def max_profit(self, prices):
        if len(prices) == 0:
            return 0
        min_price = prices[0]
        res = 0
        for price in prices:
            res = max(res, price-min_price)
            min_price = min(min_price, price)
        return res



if __name__ == "__main__":
    so = Solution()
    num = [2,1]
    print so.max_profit(num)

