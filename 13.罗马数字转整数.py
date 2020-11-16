#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        """通常情况下，罗马数字中小的数字在大的数字的右边。
        如果当前的值大于左边的数字，则直接减去左边值乘以2（因为之前加过一个了）
        否则加上当前值
        """
        if not s:
            return 0
        roman_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = 0
        pre = 0
        for c in s:
            v = roman_values[c]
            if pre < v:
                result += v - pre * 2
            else:
                result += v
            pre = v
        return result


# @lc code=end
print(Solution().romanToInt("III"))
print(Solution().romanToInt("IV"))
print(Solution().romanToInt("IX"))
print(Solution().romanToInt("LVIII"))
print(Solution().romanToInt("MCMXCIV"))