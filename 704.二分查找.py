#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#
"""
解题思路：
1. 二分查找法
"""
from typing import List
# @lc code=start


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1
        while i <= j:
            h = (i+j)//2
            if nums[h] == target:
                return h
            elif nums[h] > target:
                j = h - 1
            else:
                i = h + 1
        return -1


# @lc code=end
print(Solution().search([-1, 0, 3, 5, 9, 12], 9))
print(Solution().search([-1, 0, 3, 5, 9, 12], -2))
