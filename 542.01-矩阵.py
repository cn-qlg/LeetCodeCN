#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#
""" 
解题思路：
1. f(i,j)表示第i行第j列元素mat[i][j]到最近的0的距离。则，有以下几种情况：
    a. 如果mat[i][j]=0，那么f(i,j)=0
    b. 如果mat[i][j]上下左右4个方向上相邻节点为0，则f(i,j)=1
    c. 如果mat[i][j]上下左右4个方向上相邻节点都不为0，则f(i,j)=min(f(i-1,j),f(i+1,j),f(i,j-1),f(i,j+1))
"""
from typing import List
# @lc code=start


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        MAX_DIS = 99999
        m, n = len(mat), len(mat[0])
        res = [[MAX_DIS]*n for _ in range(m)]

        nodes = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                elif mat[i][j] == 1:
                    isZeroFound = False
                    for p, q in self.getNeighbors(i,j,m,n):
                        if mat[p][q] == 0:
                            res[i][j] = 1
                            isZeroFound = True
                            break
                    if not isZeroFound:
                        nodes.append((i,j))
                else:
                    nodes.append((i,j))
        while nodes:
            i,j = nodes.pop(0)
            for p, q in self.getNeighbors(i,j,m,n):
                if res[i][j] > res[p][q] + 1:
                    res[i][j] = res[p][q] + 1
            if res[i][j] == MAX_DIS:
                nodes.append((i,j))
        return res

    def getNeighbors(self, i, j, m, n):
        for p, q in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= p < m and 0 <= q < n:
                yield p, q


# @lc code=end
"""
0 0 0 
0 1 0
1 1 1
1 1 1
---------
0 0 0
0 1 0
1 x 1
x x x

0 0 0 
0 1 0
1 1 1
1 0 1
---------
0 0 0
0 1 0
1 x 1
x x x
"""
# print(Solution().updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
# print(Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
# print(Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1],[1,1,1]]))
print(Solution().updateMatrix([[1,1,0,1,1,1,1,1,1,1],[1,1,0,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,1,1,0],[1,1,1,1,1,1,0,0,1,0]]))
# print(Solution().updateMatrix([[1,1,0,1,1,1,1,1,1,1],[1,1,0,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,1,1,0],[1,1,1,1,1,1,0,0,1,0],[1,0,0,1,1,1,0,1,0,1],[0,0,1,0,0,1,1,0,0,1],[0,1,0,1,1,1,1,1,1,1],[1,0,0,1,1,0,0,0,0,0],[0,0,1,1,1,1,0,1,1,1],[1,1,0,0,1,0,1,0,1,1]]))