#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        重复子串，相当于求长度的因素。
        """
        for i in range(1, len(s)//2+1):
            if len(s)%i == 0:
                count = len(s) // i 
                if s[0:i]*count == s:
                    return True
        return False
        
# @lc code=end

if __name__ == "__main__":
    print(Solution().repeatedSubstringPattern("abab"))
    print(Solution().repeatedSubstringPattern("aaa"))
    print(Solution().repeatedSubstringPattern("aba"))
    print(Solution().repeatedSubstringPattern("abcabcabcabc"))