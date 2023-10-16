#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#
from typing import List

# @lc code=start
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        nums = {"1","2","3","4","5","6","7","8","9","0"}
        def backtrack(index, path:str):
            if index == len(s):
                res.append(path)
                return
            if s[index] not in nums:
                backtrack(index+1, path+s[index].lower())
                backtrack(index+1, path+s[index].upper())
            else:
                backtrack(index+1,  path+s[index])
        
        backtrack(0, "")
        return res
                

# @lc code=end
print(Solution().letterCasePermutation("a1b2"))
print(Solution().letterCasePermutation("3z4"))
