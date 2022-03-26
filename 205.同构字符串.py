#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = dict()
        map2 = dict()
        if len(s) != len(t):
            return False
        for i, c in enumerate(s):
            if t[i] in map1:
                if map1[t[i]] != c:
                    return False
            else:
                map1[t[i]] = c
            if c in map2:
                if map2[c] != t[i]:
                    return False
            else:
                map2[c] = t[i]
        return True
# @lc code=end


if __name__ == "__main__":
    print(Solution().isIsomorphic("badc", "baba") == False)
    print(Solution().isIsomorphic("foo", "bar") == False)
