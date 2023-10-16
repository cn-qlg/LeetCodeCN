#
# @lc app=leetcode.cn id=70 lang=python
#
# [70] 爬楼梯
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        f(x) = f(x-1) + f(x-2)
        =>
        f(0) = 0
        f(1) = 1
        f(2) = 2
        f(3) = 3
        """
        p = 0
        q = 0
        r = 1
        for i in range(1,n+1):
            p = q
            q = r
            r = p + q
        return r


# @lc code=end
if __name__ == "__main__":
    print(Solution().climbStairs(1))
    print(Solution().climbStairs(2))
    print(Solution().climbStairs(3))
    print(Solution().climbStairs(4))
