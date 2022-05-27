#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#
""" 
解题思路：
1. 直接不断除以2，如果中间某个数不能被2整除，则说明，不是2的幂。否则一定会除到1为止。
2. 
"""
# @lc code=start
class Solution:
    # def isPowerOfTwo(self, n: int) -> bool:
    #     if n <= 0:
    #         return False
    #     while n > 1 or n < -1:
    #         if n %2 != 0:
    #             return False
    #         n = n //2
    #     return True
    
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0

# @lc code=end
print(Solution().isPowerOfTwo(1))
print(Solution().isPowerOfTwo(16))
print(Solution().isPowerOfTwo(3))
print(Solution().isPowerOfTwo(4))
print(Solution().isPowerOfTwo(5))
print(Solution().isPowerOfTwo(-16))
"""
10
100
1000
10000
"""