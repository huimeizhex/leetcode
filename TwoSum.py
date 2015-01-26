class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        mid = {}
        for i in range(len(num)):
            if num[i] in mid:
                mid[num[i]].append(i+1)
            else:
                mid[num[i]] = [i+1]

        for key in mid:
            other = target - key
            if other in mid:
                if key == other:
                    res, ans =  mid[key][0], mid[key][1]
                else:
                    res, ans =  mid[key][0],mid[other][0]
                if res > ans:
                    res, ans = ans, res
                return res, ans
