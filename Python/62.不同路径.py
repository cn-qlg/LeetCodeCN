#
# @lc app=leetcode.cn id=62 lang=python
#
# [62] 不同路径
#

# @lc code=start
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        """解题思路
        f(i,j)表示到达位置第i，j共有所少条不同的路径
        其中f(0,0)=0
        f(0,1)=f(0,2)=……=f(0,n)=1
        f(1,0)=f(2,0)=……=f(m,0)=1
        对于边界以外的点：有f(i,j)=f(i-1,j)+f(i,j-1)
        """
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            res[i][0] = 1
        for j in range(n):
            res[0][j] = 1
        # printMatrix(res, m)
        for i in range(1,m):
            for j in range(1, n):
                res[i][j] = res[i-1][j] + res[i][j-1]
            # printMatrix(res, m)
        return res[i][j]

# def printMatrix(res, m):
#     for i in range(m):
#         print(res[i])
#     print("-"* 10)
# @lc code=end
print(Solution().uniquePaths(3,7))
print(Solution().uniquePaths(3,2))
print(Solution().uniquePaths(7,3))
print(Solution().uniquePaths(3,3))

