#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#
""" 
解题思路：
1. """
# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1 or n < -1:
            if n %2 != 0:
                return False
            n = n //2
        return True
# @lc code=end
print(Solution().isPowerOfTwo(1))
print(Solution().isPowerOfTwo(16))
print(Solution().isPowerOfTwo(3))
print(Solution().isPowerOfTwo(4))
print(Solution().isPowerOfTwo(5))
print(Solution().isPowerOfTwo(-16))
