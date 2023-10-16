#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#
"""
解题思路：
1. 常规解法，一次判断每一行，每一列，每一个小九宫格是否有重复的数。
2. 分别用一个二维数组存储第i行（第j列）数字重复次数，再用一个三位数组，记录第(i//3,j//3)个九宫格内数字重复次数。如果重复次数大于1，则说明不符合要求。
"""
from typing import List
# @lc code=start
class Solution:
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     for i in range(9):
    #         for j in range(9):
    #             if board[i][j] == ".":
    #                 continue

    #             # 判断横向
    #             nums = set()
    #             for k in range(9):
    #                 if board[i][k] != ".":
    #                     if board[i][k] in nums:
    #                         return False
    #                     else:
    #                         nums.add(board[i][k])

    #             # 判断竖向
    #             nums = set()
    #             for k in range(9):
    #                 if board[k][j] != ".":
    #                     if board[k][j] in nums:
    #                         return False
    #                     else:
    #                         nums.add(board[k][j])

    #             # 判断单元格
    #             nums = set()
    #             xs = [x + (i//3)*3 for x in [0,1,2]]
    #             ys = [y + (j//3)*3 for y in [0,1,2]]
    #             for x in xs:
    #                 for y in ys:
    #                     if board[x][y] != ".":
    #                         if board[x][y] in nums:
    #                             return False
    #                         else:
    #                             nums.add(board[x][y])
    #     return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0] * 9 for _ in range(9)]
        columns = [[0] * 9 for _ in range(9)]
        subboxes = [[[0] * 9 for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                n = int(board[i][j])-1
                rows[i][n] += 1
                columns[j][n] += 1
                subboxes[i//3][j//3][n] += 1
                if rows[i][n] > 1 or columns[j][n] > 1 or subboxes[i//3][j//3][n] > 1:
                    return False
        return True


# @lc code=end
print(Solution().isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

print(Solution().isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))