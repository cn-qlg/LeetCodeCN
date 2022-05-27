#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        bigInt = 2147483648
        cnt = 0
        while n > 0:
            if n >= bigInt:
                cnt += 1
                n -= bigInt
            bigInt = bigInt //2
        return cnt
# @lc code=end
print(Solution().hammingWeight(31))
print(Solution().hammingWeight(32))