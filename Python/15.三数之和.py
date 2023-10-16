#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
"""
解题思路：
1. 三重for循环，配合条件过滤，提前break（有超时风险）
"""
from typing import List
# @lc code=start


class Solution:
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     nums.sort()
    #     res = []
    #     s = set()
    #     for i,m in enumerate(nums):
    #         if m >0:
    #             break
    #         for j in range(i+1, len(nums)):
    #             if m + nums[j] > 0:
    #                 break
    #             for k in range(j+1, len(nums)):
    #                 n = nums[j]
    #                 o = nums[k]
    #                 if m + n + o == 0:
    #                     if f"{m}-{n}-{o}" in s:
    #                         continue
    #                     res.append([m,n,o])
    #                     s.add(f"{m}-{n}-{o}")
    #                 elif m + n + 0 > 0:
    #                     break
    #     return res
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            k = n - 1
            target = -nums[i]
            for j in range(i+1, n-1):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                while nums[j] + nums[k] > target and j < k:
                    k -= 1
                if j == k:
                    break
                if nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
        return res


# @lc code=end
print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
print(Solution().threeSum([]))
print(Solution().threeSum([0]))
print(Solution().threeSum([0,0,0]))
