#
# @lc app=leetcode.cn id=64 lang=python
#
# [64] 最小路径和
#

# @lc code=start
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        MAX = 999
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                up = left = MAX
                if i - 1>=0:
                    up = grid[i-1][j]
                if j - 1>=0:
                    left = grid[i][j-1]
                grid[i][j] += min(up, left)
                # print(i, j, grid)

        return grid[-1][-1]


# @lc code=end
print(Solution().minPathSum([[0, 0], [0, 0]]))
print(Solution().minPathSum([[1, 2, 3], [4, 5, 6]]))
