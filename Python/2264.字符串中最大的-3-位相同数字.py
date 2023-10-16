#
# @lc app=leetcode.cn id=2264 lang=python3
#
# [2264] 字符串中最大的 3 位相同数字
#

# @lc code=start
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i, n = 0, len(num)-2
        m = -1
        ms = ""
        while i < n:
            if num[i] == num[i+1] == num[i+2]:
                if int(num[i:i+3]) > m:
                    m = int(num[i:i+3])
                    ms = num[i:i+3]
                i += 3
            else:
                i += 1
        return ms
# @lc code=end
print(Solution().largestGoodInteger("6777133339"))
print(Solution().largestGoodInteger("2300019"))
print(Solution().largestGoodInteger("42352338"))
print(Solution().largestGoodInteger("222"))