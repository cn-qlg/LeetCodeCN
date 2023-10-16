#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
from typing import List
# @lc code=start


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        first_words = strs[0]
        for index, c in enumerate(first_words):
            for word in strs[1:]:
                if len(word) == index or word[index] != c:
                    return first_words[0:index]
        return first_words

    # def longestCommonPrefix_1(self, strs: List[str]) -> str:
    #     if not strs or len(strs) == 0:
    #         return ""
    #     longest_length = -1
    #     first_words = strs[0]
    #     for index, c in enumerate(first_words):
    #         for word in strs[1:]:
    #             if len(word) -1 >= index and word[index] == c:
    #                 pass
    #             else:
    #                 if longest_length == -1:
    #                     return ""
    #                 else:
    #                     return first_words[0:longest_length + 1]
    #         else:
    #             longest_length += 1
    #     return first_words[0:longest_length + 1]

# @lc code=end


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
