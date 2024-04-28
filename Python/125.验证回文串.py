#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) -1
        while True:
            if i >= j:
                break

            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].upper() != s[j].upper():
                return False
            i += 1
            j -= 1
        return True
    
if __name__ == "__main__":
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
    print(Solution().isPalindrome("race a car"))
    print(Solution().isPalindrome(" "))
    print(Solution().isPalindrome("A"))

