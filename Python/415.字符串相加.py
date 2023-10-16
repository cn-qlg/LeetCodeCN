#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    # def addStrings(self, num1: str, num2: str) -> str:
    #     i = len(num1) - 1
    #     j = len(num2) - 1
    #     k = 0
    #     s = 0
    #     c = 0
    #     while i >= 0 and j >=0:
    #         m = int(num1[i]) + int(num2[j]) + c
    #         c = m // 10
    #         m = m % 10
    #         s = m * 10 ** k + s
    #         i -= 1
    #         j -= 1
    #         k += 1
    #     while i >=0:
    #         m = int(num1[i]) + c
    #         c = m // 10
    #         m = m % 10
    #         s = m * 10 ** k + s
    #         i -= 1
    #         k += 1
        
    #     while j >=0:
    #         m = int(num2[j]) + c
    #         c = m // 10
    #         m = m % 10
    #         s = m * 10 ** k + s
    #         j -= 1
    #         k += 1
    #     if c != 0:
    #         s = c * 10 ** k + s
    #     return str(s)
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        c = 0
        s = ""
        while i >=0 or j >=0 or c > 0:
            m = int(num1[i]) if i >=0 else 0
            n = int(num2[j]) if j >=0 else 0
            t = m + n + c
            c = t // 10
            t = t % 10
            s = str(t) + s
            i -= 1
            j -= 1
        return s
            

# @lc code=end
print(Solution().addStrings("11","123"))
print(Solution().addStrings("456","77"))
print(Solution().addStrings("0","0"))
print(Solution().addStrings("9999","1"))
print(Solution().addStrings("9999","0"))