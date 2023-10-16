#
# @lc app=leetcode.cn id=119 lang=python
#
# [119] 杨辉三角 II
#

# @lc code=start


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        """解法思路
        1
        1 1
        1 2 1
        1 3 3 1
        1 4 6 4 1
        1 5 10 10 5 1
        """
        if rowIndex == 0:
            return [1]
        res = [1]
        for i in range(1, rowIndex+1):
            res.append(1)
            for j in range(i-1, 0, -1):
                res[j] = res[j] + res[j-1]
        return res


# @lc code=end
print(Solution().getRow(0))
print(Solution().getRow(1))
print(Solution().getRow(2))
print(Solution().getRow(3))
print(Solution().getRow(4))
print(Solution().getRow(5))
