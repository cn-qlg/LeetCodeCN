#
# @lc app=leetcode.cn id=961 lang=python3
#
# [961] 在长度 2N 的数组中找出重复 N 次的元素
#
from typing import List
# @lc code=start
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            if n in s:
                return n
            else:
                s.add(n)
        
# @lc code=end
print(Solution().repeatedNTimes([1,2,3,3]))
print(Solution().repeatedNTimes([2,1,2,5,3,2]))
print(Solution().repeatedNTimes([5,1,5,2,5,3,5,4]))
