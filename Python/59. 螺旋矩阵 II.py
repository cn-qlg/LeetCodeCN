"""
解题思路：
1. 与54.螺旋矩阵基本差不多
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        left, right, top, bottom = 0, n-1, 0, n-1
        nums = n **2
        x = 1
        while x <= nums:
            for i in range(left, right+1):
                res[top][i] = x
                x += 1
            top += 1

            for i in range(top, bottom+1):
                res[i][right] = x
                x += 1
            right -= 1

            if top <= bottom:
                for i in range(right, left-1, -1):
                    res[bottom][i] = x
                    x += 1
            bottom -= 1
            
            if left <= right:
                for i in range(bottom, top -1, -1):
                    res[i][left] = x
                    x += 1
            left += 1

        return res
    

if __name__ == "__main__":
    print(Solution().generateMatrix(2))
    print(Solution().generateMatrix(3))
    print(Solution().generateMatrix(4))

    """
    1  2  3  4
    12 13 14 5
    11 16 15 6
    10 9  8  7
    """