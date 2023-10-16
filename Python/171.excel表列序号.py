#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        values = {
            "A":1,
            "B":2,
            "C":3,
            "D":4,
            "E":5,
            "F":6,
            "G":7,
            "H":8,
            "I":9,
            "J":10,
            "K":11,
            "L":12,
            "M":13,
            "N":14,
            "O":15,
            "P":16,
            "Q":17,
            "R":18,
            "S":19,
            "T":20,
            "U":21,
            "V":22,
            "W":23,
            "X":24,
            "Y":25,
            "Z":26
        }
        unit = 0
        result = 0
        for c in s[::-1]:
            result = result + values[c] * (26**unit)
            unit += 1
        return result


# @lc code=end


print(1, Solution().titleToNumber("A"))
print(26, Solution().titleToNumber("Z"))
print(28, Solution().titleToNumber("AB"))
print(52, Solution().titleToNumber("AZ"))
print(78, Solution().titleToNumber("BZ"))
print(701, Solution().titleToNumber("ZY"))
print(702, Solution().titleToNumber("ZZ"))
print(703, Solution().titleToNumber("AAA"))
print(704, Solution().titleToNumber("AAB"))
print(728, Solution().titleToNumber("AAZ"))
