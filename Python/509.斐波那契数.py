#
# @lc app=leetcode.cn id=509 lang=python
#
# [509] 斐波那契数
#

# @lc code=start
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        p = 0
        q = 1
        r = p + q
        for _ in range(2,n+1):
            r = p + q
            p = q
            q = r
        return r


# @lc code=end
if __name__ == "__main__":
    # print(Solution().fib(0))
    # print(Solution().fib(1))
    print(Solution().fib(2))
    print(Solution().fib(3))
    print(Solution().fib(4))
    print(Solution().fib(5))
    print(Solution().fib(6))

