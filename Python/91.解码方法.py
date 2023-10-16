#
# @lc app=leetcode.cn id=91 lang=python
#
# [91] 解码方法
#

# @lc code=start
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        """解题思路
        f(i)表示从0-i个字符，总共的解码方法总数
        如果s[i]!=0，则f(i)=f(i-1)
        并且，如果s[i-1]!=0且s[i-1]*10+s[i]<=26，则f(i)+=f(i-2)
        """
        if s[0] == "0":
            return 0
        res = [1] + [0] * len(s)
        nums = [int(c) for c in s]
        length = len(nums)
        for i in range(1, length+1):
            if nums[i-1] != 0:
                res[i] += res[i-1]
            if i >= 2 and nums[i-2] != 0 and nums[i-2] * 10 + nums[i-1] <= 26:
                res[i] += res[i-2]
            # print(res)
        # print("-"*10)
        return res[-1]


# @lc code=end
print(Solution().numDecodings("12"))
print(Solution().numDecodings("226"))
print(Solution().numDecodings("0"))
print(Solution().numDecodings("11106"))
print(Solution().numDecodings("1123"))

"""
1123
1 1 2 3
11 2 3
1 12 3
1 1 23
11 23

"""
