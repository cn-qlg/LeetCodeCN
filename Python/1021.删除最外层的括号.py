#
# @lc app=leetcode.cn id=1021 lang=python3
#
# [1021] 删除最外层的括号
#
"""
解题思路：
1. 通过栈来做括号匹配，如果在某次右括号匹配过程中，发现栈为空，说明之前的括号都是完全匹配的，然后分别移除前后两个括号即可。
"""
# @lc code=start


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        pre = 0
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(c)
            else:
                stack.pop()
                if len(stack) == 0:
                    res.append(s[pre+1: i])
                    pre = i + 1
        return "".join(res)


# @lc code=end
"""
(()())(())
(()())(())(()(()))
"""
print(Solution().removeOuterParentheses("(()())(())"))
print(Solution().removeOuterParentheses("(()())(())(()(()))"))
print(Solution().removeOuterParentheses("()()"))
