#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        say = ["1"]
        for _ in range(2, n+1):
            pre = say[0]
            count = 1
            cur_say = []
            for c in say[1:]:
                if c == pre:
                    count +=1
                else:
                    cur_say.extend([str(count), pre])
                    pre = c
                    count = 1
            cur_say.extend([str(count), pre])
            say = cur_say
        return "".join(say)
                
# @lc code=end
print(Solution().countAndSay(1))
print(Solution().countAndSay(2))
print(Solution().countAndSay(3))
print(Solution().countAndSay(4))
print(Solution().countAndSay(5))