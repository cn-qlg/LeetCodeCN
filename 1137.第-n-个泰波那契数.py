#
# @lc app=leetcode.cn id=1137 lang=python
#
# [1137] 第 N 个泰波那契数
#

# @lc code=start
import re


class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        
        t0, t1, t2 = 0,1,1
        for _ in range(3, n+1):
            t3 = t0 + t1 + t2
            t0, t1, t2 = t1, t2, t3
        return t3
# @lc code=end

print(Solution().tribonacci(3))
print(Solution().tribonacci(4))
print(Solution().tribonacci(5))
print(Solution().tribonacci(25))