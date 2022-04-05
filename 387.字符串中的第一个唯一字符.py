#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        charIndex = dict()
        for c in s:
            if c in charIndex:
                charIndex[c] += 1
            else:
                charIndex[c] = 1
        for i, c in enumerate(s):
            if charIndex[c] == 1:
                return i
        return -1
# @lc code=end


if __name__ == "__main__":
    print(Solution().firstUniqChar("leetcode"))
    print(Solution().firstUniqChar("loveleetcode"))
    print(Solution().firstUniqChar("aabb"))
