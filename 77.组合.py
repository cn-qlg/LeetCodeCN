#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
from typing import List, Set
# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(c, nums:List[int], used:Set[int]):
            if len(nums) == k:
                res.append(nums[:])
                return
            for i in range(c,n+1):
                if i not in used:
                    nums.append(i)
                    used.add(i)
                    backtrack(i, nums, used)
                    nums.pop()
                    used.remove(i)
                    used.copy()
        
        backtrack(1, [],set())
        return res
# @lc code=end
print(Solution().combine(4,2))
print(Solution().combine(1,1))
print(Solution().combine(4,3))

