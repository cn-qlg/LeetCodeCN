#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        stack = []
        for c in s:
            if c in ['(','[','{']:
                stack.append(c)
                continue
            if len(stack) <= 0:
                return False
            head = stack.pop()
            if c == ')' and head == '(':
                continue
            if c == ']' and head == '[':
                continue
            if c == '}' and head == '{':
                continue
            return False
        if len(stack) > 0:
            return False
        return True
        
# @lc code=end
print(Solution().isValid("()"))
print(Solution().isValid("()[]{}"))
print(Solution().isValid("(]"))
print(Solution().isValid("([)]"))
print(Solution().isValid("{[]}"))
print(Solution().isValid("]"))
