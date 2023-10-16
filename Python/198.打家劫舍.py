#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
from typing import List
""" 
解题思路：
1. r(i)表示第i个房间的现金金额，f(i)表示到第i个房间时，已偷取的现金数量（包含第i个房间）。
f(i)有两种可能：
    a. 偷取第i个房间的现金，则f(i)=f(i-2)+r(i)
    b. 不偷，则f(i)=f(i-1)
"""
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        nums[1] = max(nums[0],nums[1])
        for i, n in enumerate(nums):
            if i >= 2:
                nums[i] = max(nums[i-2]+n, nums[i-1])
        return max(nums[-2:])
# @lc code=end
print(Solution().rob([1,2,3,1]))
print(Solution().rob([2,7,9,3,1]))
print(Solution().rob([2,1,1,2]))
