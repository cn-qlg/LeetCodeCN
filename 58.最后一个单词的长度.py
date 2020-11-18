#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for c in s[::-1]:
            if c == ' ':
                if count >0:
                    return count
            else:
                count +=1
        return count

    # def lengthOfLastWord(self, s: str) -> int:
    #     """从左向右遍历"""   
    #     len = cur_len = 0
    #     for c in s:
    #         if c != ' ':
    #             cur_len += 1
    #         else:
    #             if cur_len >0:
    #                 len = cur_len
    #             cur_len = 0
    #     if cur_len >0:
    #         len = cur_len
    #     return len
        

    # def lengthOfLastWord_1(self, s: str) -> int:
    #     """直接调用string.split方法"""
    #     words = s.split(' ')
    #     if not words:
    #         return 0
    #     for word in words[::-1]:
    #         if word:
    #             return len(word)
    #     return 0
        
# @lc code=end
print(Solution().lengthOfLastWord("Hello World"))
print(Solution().lengthOfLastWord("Hello"))
print(Solution().lengthOfLastWord(""))
print(Solution().lengthOfLastWord("  "))
print(Solution().lengthOfLastWord("a aa aaa  "))
# 1 2 34 5
# 01234567