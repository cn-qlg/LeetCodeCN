#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#
"""
解题思路：
1. 直接计算，后排序
2. 先找到第一个大于0的数，依次为坐标，分别向两头扩展，并判断大小。这样小的就直接放在最前面了。
3. 从两端开始，
    3.1 先初始化一个长度为n的数组，然后比较的结果大的先放在后面，依次往前放。
    3.2 计算结果按从大到小放，后面逆序一下
"""
from typing import List
# @lc code=start
class Solution:
    # 3.1
    # def sortedSquares(self, nums: List[int]) -> List[int]:
    #     ans = [0]*len(nums)
    #     i,j = 0, len(nums)-1
    #     p = j
    #     while i <=j:
    #         if nums[i]**2 >= nums[j]**2:
    #             ans[p]= nums[i]**2
    #             i +=1
    #         else:
    #             ans[p] = nums[j]**2
    #             j -=1
    #         p -= 1
    #     return ans
    
    # 3.2
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        i,j = 0, len(nums)-1
        while i <=j:
            if nums[i]**2 >= nums[j]**2:
                ans.append(nums[i]**2)
                i +=1
            else:
                ans.append(nums[j]**2)
                j -=1
        return ans[::-1]

        
# @lc code=end
print(Solution().sortedSquares([-4,-1,0,3,10]))
print(Solution().sortedSquares([-7,-3,2,3,11]))