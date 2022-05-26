#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
from typing import List, Set
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def _permute(path :List[int], used:Set[int]):
            if len(used) == len(nums):
                res.append(path[:])
                return
            for n in nums:
                if n not in used:
                    path.append(n)
                    used.add(n)
                    _permute(path, used)
                    path.pop()
                    used.remove(n)

        _permute(list(), set())
        return res

        
# @lc code=end
print(Solution().permute([1,2,3]))
print(Solution().permute([0,1]))
print(Solution().permute([1,2,3,4]))