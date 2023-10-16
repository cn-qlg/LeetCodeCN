#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
from typing import List
# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l <= r:
            mid = (r-l)//2 + l
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        if l >= len(nums):
            return l
        if nums[l] < target:
            return l + 1
        return l
# @lc code=end
print(Solution().searchInsert([1,3,5,6],5))
print(Solution().searchInsert([1,3,5,6],2))
print(Solution().searchInsert([1,3,5,6],7))
print(Solution().searchInsert([1,3,5,6],0))

