#
# @lc app=leetcode.cn id=1646 lang=python
#
# [1646] 获取生成数组中的最大值
#

# @lc code=start
class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        res = [0,1]
        maxNum = 1
        for i in range(2, n + 1):
            if i % 2 == 0:
                res.append(res[i//2])
            else:
                t = res[i//2] + res[i//2 + 1]
                if t > maxNum:
                    maxNum = t
                res.append(t)
        return maxNum
# @lc code=end
print(Solution().getMaximumGenerated(7))
