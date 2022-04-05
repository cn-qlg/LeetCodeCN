#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d1 = dict()
        for c in s:
            if c not in d1:
                d1[c] = 1
            else:
                d1[c] += 1
        
        d2 = dict()
        
        for c in t:
            if c not in d2:
                d2[c] = 1
            else:
                d2[c] += 1
        
        for k, v in d2.items():
            if k not in d1 or d1[k]!= v:
                return k
        

        
# @lc code=end
if __name__ == "__main__":
    print(Solution().findTheDifference("abcd","abcde"))
    print(Solution().findTheDifference("","t"))

