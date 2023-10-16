#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
from typing import List
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0, len(height)-1
        ans = 0
        while i < j:
            ans=max(ans,min(height[i], height[j]) * (j-i))
            if height[i] >= height[j]:
                j-=1
            else:
                i += 1
        return ans

# @lc code=end
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
print(Solution().maxArea([1,1]))
