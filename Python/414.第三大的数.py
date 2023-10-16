#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#
from typing import List
"""解题思路：
1. 先找出3个不同的数字，然后最大为p，中间的为q，最小的位r。再遍历数组，分别更新这三个值。即可

2. 
"""
# @lc code=start


class Solution:
    # def thirdMax(self, nums: List[int]) -> int:
    #     if len(nums) <3:
    #         return max(nums)
    #     s = set()
    #     index = 0
    #     for index,n in enumerate(nums):
    #         if n not in s:
    #             s.add(n)
    #         if len(s) >= 3:
    #             break
    #     if len(s) < 3:
    #         return max(s)
    #     p = max(s)
    #     r = min(s)
    #     q = sum(s)-p-r

    #     for i in range(index+1, len(nums)):
    #         if nums[i] > p:
    #             p,q,r = nums[i],p,q
    #         elif nums[i] == p:
    #             continue
    #         elif nums[i] > q:
    #             q,r = nums[i],q
    #         elif nums[i] == q:
    #             continue
    #         elif nums[i] > r:
    #             r = nums[i]
    #     # print(p,q,r)
    #     return r
    def thirdMax(self, nums: List[int]) -> int:
        p = q = r = None
        for n in nums:
            if p is None or n > p:
                p, q, r = n, p, q
            elif n == p:
                continue
            elif q is None or q < n < p:
                q, r = n, q
            elif n == q:
                continue
            elif r is None or r < n < q:
                r = n
        # print(p, q, r)
        if r is None:
            return p
        return r


# @lc code=end
print(Solution().thirdMax([3, 2, 1]))
print(Solution().thirdMax([1, 2]))
print(Solution().thirdMax([2, 2, 3, 1]))
print(Solution().thirdMax([1, 1, 2]))
print(Solution().thirdMax([1, 2, 2, 5, 3, 5]))
