#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#
from typing import List
# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) -1
        while i< j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
# @lc code=end

if __name__ == "__main__":
    Solution().reverseString(["h","e","l","l","o"])