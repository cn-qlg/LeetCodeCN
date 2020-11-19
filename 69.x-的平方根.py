#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        high = x //2 + 1
        low = 1
        mid = (high + low) //2
        while low <= high:
            if mid ** 2 < x:
                low = mid + 1
            elif mid ** 2 > x:
                high = mid - 1
            else:
                return mid
            mid = (high + low) //2
        return high


# @lc code=end
print(Solution().mySqrt(1))
print(Solution().mySqrt(4))
print(Solution().mySqrt(5))
print(Solution().mySqrt(6))
print(Solution().mySqrt(8))
print(Solution().mySqrt(9))
print(Solution().mySqrt(1614691295))
