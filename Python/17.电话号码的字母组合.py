#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
from typing import List
# @lc code=start


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numsToAlphs = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def dfs(index, path, res:List[str]):
            if index >= len(digits):
                if path :
                    res.append(path)
                return res
            
            for c in numsToAlphs[digits[index]]:
                res = dfs(index+1, path + c, res)
            
            return res
        res = dfs(0, "", [])
        return res
# @lc code=end
print(Solution().letterCombinations("23"))
print(Solution().letterCombinations(""))
print(Solution().letterCombinations("2"))
print(Solution().letterCombinations("234"))
