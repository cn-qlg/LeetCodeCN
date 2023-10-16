#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#
""" 
解题思路：
1. 依次遍历每个点，如果当前点为1，则才用广度优先算法，计算当前岛屿的面积。并把遍历过的点置为0，防止重复遍历。
"""
from typing import List
# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])

        max_area = 0
        for i in range(h):
            for j in range(w):
                nodes = []
                if grid[i][j] == 1:
                    nodes.append((i,j))
                cnt = 0
                while nodes:
                    p, q = nodes.pop()
                    if grid[p][q] == 1:
                        grid[p][q] = 0
                        cnt += 1
                    for m, n in [(p-1,q),(p+1, q), (p, q-1), (p, q+1)]:
                        if 0 <= m < h and 0<=n<w and grid[m][n] == 1:
                            nodes.append((m,n))
                if cnt > max_area:
                    max_area = cnt
        return max_area

                

# @lc code=end
# print(Solution().maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
# 1 1 0 0 0
# 1 1 0 0 0
# 0 0 0 1 1
# 0 0 0 1 1
print(Solution().maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))
