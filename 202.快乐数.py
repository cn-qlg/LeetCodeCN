#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        total_result = set()
        while True:
            chars = str(n)
            n = 0
            for c in chars:
                n += int(c)**2
            if n == 1:
                return True
            if n in total_result:
                return False
            else:
                total_result.add(n)
# @lc code=end
print(Solution().isHappy(19))
print(Solution().isHappy(1))
print(Solution().isHappy(2))
print(Solution().isHappy(3))
