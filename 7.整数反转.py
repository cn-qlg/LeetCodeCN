#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    # def reverse(self, x: int) -> int:
    #     max = 2147483647
    #     min = -2147483648
    #     if x < 0:
    #         sign = -1
    #         x = x*-1
    #     else:
    #         sign = 1
    #     result = sign * int(str(x)[::-1])
    #     if result > max or result < min:
    #         return 0
    #     return result
    
    def reverse(self, x: int) -> int:
        r = 0
        v = abs(x)
        while v !=0:
            q = v % 10
            v = v//10
            
            if r > 214748364 or (r == 214748364 and q >7):
                return 0
            if r < -2147483648 or (r == -2147483648 and q >8):
                return 0
            r = r *10 + q
        if x >= 0:
            return r
        else:
            return -r

# @lc code=end

# print(Solution().reverse(123))
# print(Solution().reverse(-123))
# print(Solution().reverse(120))
# print(Solution().reverse(1563847412))

print(Solution().reverse2(123))
print(Solution().reverse2(-123))
print(Solution().reverse2(120))
print(Solution().reverse2(1563847412))