#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#
""" 
解题思路：

"""
from typing import List
# @lc code=start


class Solution:
    # def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    #     MAX_DIS = 99999
    #     m, n = len(mat), len(mat[0])
    #     res = [[MAX_DIS]*n for _ in range(m)]

    #     nodes = []
    #     for i in range(m):
    #         for j in range(n):
    #             if mat[i][j] == 0:
    #                 res[i][j] = 0
    #             elif mat[i][j] == 1:
    #                 isZeroFound = False
    #                 for p, q in self.getNeighbors(i,j,m,n):
    #                     if mat[p][q] == 0:
    #                         res[i][j] = 1
    #                         isZeroFound = True
    #                         break
    #                 if not isZeroFound:
    #                     nodes.append((i,j))
    #             else:
    #                 nodes.append((i,j))
    #     while nodes:
    #         i,j = nodes.pop(0)
    #         for p, q in self.getNeighbors(i,j,m,n):
    #             if res[i][j] > res[p][q] + 1:
    #                 res[i][j] = res[p][q] + 1
    #         if res[i][j] == MAX_DIS:
    #             nodes.append((i,j))
    #     return res

    def getNeighbors(self, i, j, m, n):
        for p, q in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= p < m and 0 <= q < n:
                yield p, q

    # def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    #     zeros = []
    #     m,n = len(mat), len(mat[0])
    #     res = [[0]*n for _ in range(m)]
    #     for i in range(m):
    #         for j in range(n):
    #             if mat[i][j] == 0:
    #                 zeros.append((i,j))

    #     d = 0
    #     nodeSet = set(zeros)
    #     while zeros:
    #         newZeros = []
    #         for i,j in zeros:
    #             for p, q in self.getNeighbors(i,j,m,n):
    #                 if mat[p][q] == 1 and (p,q) not in nodeSet:
    #                     res[p][q] = d + 1
    #                     newZeros.append((p,q))
    #                     nodeSet.add((p,q))
    #         zeros = newZeros
    #         d += 1
    #     return res

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dist = [[0] * n for _ in range(m)]
        q = [(i, j) for i in range(m)
                      for j in range(n) if matrix[i][j] == 0]
        # 将所有的 0 添加进初始队列中
        seen = set(q)

        # 广度优先搜索
        while q:
            i, j = q.pop(0)
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
                    seen.add((ni, nj))

        return dist


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
print(Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
print(Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1], [1, 1, 1]]))
print(Solution().updateMatrix([[1, 1, 0, 1, 1, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1, 1, 1, 1, 1], [
      1, 1, 1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 1, 1, 1, 0, 0, 1, 0]]))
print(Solution().updateMatrix([[1, 1, 0, 1, 1, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 1, 1, 1, 0, 0, 1, 0], [1, 0, 0, 1, 1, 1, 0, 1, 0, 1], [
      0, 0, 1, 0, 0, 1, 1, 0, 0, 1], [0, 1, 0, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 1, 1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0, 1, 1, 1], [1, 1, 0, 0, 1, 0, 1, 0, 1, 1]]))
