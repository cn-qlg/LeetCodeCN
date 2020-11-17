#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        
        long_length = len(haystack)
        short_length = len(needle)
        if short_length > long_length:
            return -1
        i = 0
        while i < long_length:
            if haystack[i] == needle[0]:
                if haystack[i:i+short_length] == needle:
                    return i
            i += 1
        return -1


# @lc code=end
print(Solution().strStr("hello", "ll"))
print(Solution().strStr("aaaaa", "bba"))
print(Solution().strStr("", ""))