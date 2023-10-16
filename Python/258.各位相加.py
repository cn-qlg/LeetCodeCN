#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
from unicodedata import name


class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            sum = 0
            while num >= 10:
                sum += num % 10
                num = num // 10
            num = sum + num
            # print(num)
        return num

# @lc code=end

if __name__ == "__main__":
    print(Solution().addDigits(10))