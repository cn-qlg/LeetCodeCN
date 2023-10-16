#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
from typing import List
# @lc code=start


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = 0
        for n in nums:
            if n != 0:
                nums[i] = n
                i+= 1
        for j in range(i, length):
            nums[j] = 0
        # print(nums)
            

# @lc code=end
Solution().moveZeroes([0,1,0,3,12])
Solution().moveZeroes([0,0,0,12])
Solution().moveZeroes([0])