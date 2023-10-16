#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#
""" 
解题思路：
1. 第一轮获取所有的坏橘子，作为起始数据。然后依次每一轮进行腐烂，并将新腐烂的橘子放到一个新的队列里
"""
from typing import List
# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:        
        m,n = len(grid),len(grid[0])
        oranges = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    for p,q in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                        if 0<=p<m and 0<=q<n and grid[p][q] == 1:
                            grid[p][q] = -1
                            oranges.append((p,q))
        
        t = 0    
        while oranges:            
            newOranges = []
            for i,j in oranges:
                grid[i][j] = 2
                for p,q in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if 0<=p<m and 0<=q<n and grid[p][q] == 1:
                        grid[p][q] = -1
                        newOranges.append((p,q))
            t += 1
            if newOranges:
                oranges = newOranges
            else:
                break

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return t

# @lc code=end
print(Solution().orangesRotting( [[2,1,1],[1,1,0],[0,1,1]]))
print(Solution().orangesRotting( [[2,1,1],[0,1,1],[1,0,1]]))
print(Solution().orangesRotting( [[2,2],[1,1],[0,0],[2,0]]))
""" 
2 2
1 1
0 0
2 0
----
2 2
2 2
0 0
2 0
"""
print(Solution().orangesRotting([[0,2]]))
print(Solution().orangesRotting([[1]]))

