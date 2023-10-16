#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start

# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         """
#         同时存下s->t和t->s的映射关系。
#         """
#         map1 = dict()
#         map2 = dict()
#         if len(s) != len(t):
#             return False
#         for i, c in enumerate(s):
#             if t[i] in map1:
#                 if map1[t[i]] != c:
#                     return False
#             else:
#                 map1[t[i]] = c
#             if c in map2:
#                 if map2[c] != t[i]:
#                     return False
#             else:
#                 map2[c] = t[i]
#         return True

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """一个更pythonic的解法"""
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
# @lc code=end


if __name__ == "__main__":
    print(Solution().isIsomorphic("badc", "baba") == False)
    print(Solution().isIsomorphic("foo", "bar") == False)
    print(list(zip("foo", "bar")))
    print(set(zip("foo", "bar")))
    print(("a", "b") == ("b", "a"))
