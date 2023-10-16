#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#

# @lc code=start

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n < 2:
            return s
        max_len = 1
        begin = 0

        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for length in range(2, n + 1):
            for i in range(n):
                j = i + length - 1
                if j > n - 1:
                    break
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                    if dp[i][j] and length > max_len:
                        max_len = length
                        begin = i
        return s[begin: begin+max_len]


# @lc code=end

if __name__ == "__main__":
    print(Solution().longestPalindrome("babad"))
    print(Solution().longestPalindrome("cbbd"))
    print(Solution().longestPalindrome("aaaa"))
