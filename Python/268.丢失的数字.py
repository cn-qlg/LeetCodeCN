#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#
"""解题思路
0-n，如果一个不少的话，总和应该是(0+n)*n/2。
依次累加各个数，然后用(0+n)*n/2减去总和就可以计算出缺少的数。
"""
from typing import List
# @lc code=start


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = int((len(nums)+1)*len(nums)/2)
        s = 0
        for n in nums:
            s += n
        return total - s


# @lc code=end
print(Solution().missingNumber([3, 0, 1]))
print(Solution().missingNumber([0, 1]))
print(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(Solution().missingNumber([0]))
