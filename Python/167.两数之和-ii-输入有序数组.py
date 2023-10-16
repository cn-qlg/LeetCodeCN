#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#
""" 
解题思路：
1. 分别从两遍往中间遍历，如果相加等于target，则直接返回，否则，如果大于target，右边index-1，否则，左边index+1。直到两个坐标相等，表示没找到"""
from typing import List
# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0, len(numbers)-1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
        
# @lc code=end
print(Solution().twoSum([2,7,11,15],9))
print(Solution().twoSum([2,3,4],6))
print(Solution().twoSum([-1,0],-1))
