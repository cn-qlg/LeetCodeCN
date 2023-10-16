#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#
"""
解题思路：
如果想构成回文串，那同一个字符的个数应该是偶数个。但是有一个特例，就是长度为奇数的回文串，中间的字符是可以只有一个的。
"""
# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        h = dict()
        for c in s:
            if c in h:
                h[c]+=1
            else:
                h[c] = 1
        extra = False
        res = 0
        for _, v in h.items():
            if v % 2 != 0:
                extra = True
            res += (v //2)*2
        if extra:
            return res +1
        return res
# @lc code=end
print(Solution().longestPalindrome("abccccdd"))
print(Solution().longestPalindrome("a"))
print(Solution().longestPalindrome("bb"))
