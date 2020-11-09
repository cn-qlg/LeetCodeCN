#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        max = 2147483647
        min = -2147483648
        if x < 0:
            sign = -1
            x = x*-1
        else:
            sign = 1
        result = sign * int(str(x)[::-1])
        if result > max or result < min:
            return 0
        return result

# @lc code=end

# print(Solution().reverse(123))
# print(Solution().reverse(-123))
# print(Solution().reverse(120))
# print(Solution().reverse(1563847412))