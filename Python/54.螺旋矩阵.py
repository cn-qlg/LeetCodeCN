"""
解题思路：
方法一：
    1. 使用递归方法，模拟循环，代码写起来比较长。
方法二：
    1. 把整个遍历看成多个外圈遍历，一圈一圈，然后每一圈分别从左到右，从上到下，从右往左，从下到上。
"""
from typing import List


class Solution:
    EmptyValue = 999

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])                

        def right(matrix: List[List[int]], i:int, j:int):            
            if i < 0 or i >= m:
                return []
            if j < 0 or j >= n:
                return []            
            if matrix[i][j] == Solution.EmptyValue:
                return []
            
            res = []
            while True:
                if 0 <= i < m and 0 <= j < n and matrix[i][j] != Solution.EmptyValue:
                    res.append(matrix[i][j])
                    matrix[i][j] = Solution.EmptyValue
                    j += 1
                else:
                    j -= 1
                    break
            others = down(matrix, i+1, j)
            res.extend(others)
            return res
       
        
        def down(matrix: List[List[int]], i:int, j:int):
            if i < 0 or i >= m:
                return []
            if j < 0 or j >= n:
                return []
            if matrix[i][j] == Solution.EmptyValue:
                return []
            
            res = []
            while True:
                if 0 <= i < m and 0 <= j < n and matrix[i][j] != Solution.EmptyValue:
                    res.append(matrix[i][j])
                    matrix[i][j] = Solution.EmptyValue
                    i += 1
                else:
                    i -= 1
                    break
            others = left(matrix, i, j-1)
            res.extend(others)
            return res
    
        def up(matrix: List[List[int]], i:int, j:int):
            if i < 0 or i >= m:
                return []
            if j < 0 or j >= n:
                return []
            if matrix[i][j] == Solution.EmptyValue:
                return []
            
            res = []
            while True:
                if 0 <= i < m and 0 <= j < n and matrix[i][j] != Solution.EmptyValue:
                    res.append(matrix[i][j])
                    matrix[i][j] = Solution.EmptyValue
                    i -= 1
                else:
                    i += 1
                    break
            others = right(matrix, i, j+1)
            res.extend(others)
            return res
        
        def left(matrix: List[List[int]], i:int, j:int):
            if i < 0 or i >= m:
                return []
            if j < 0 or j >= n:
                return []
            if matrix[i][j] == Solution.EmptyValue:
                return []
            
            res = []
            while True:
                if 0 <= i < m and 0 <= j < n and matrix[i][j] != Solution.EmptyValue:
                    res.append(matrix[i][j])
                    matrix[i][j] = Solution.EmptyValue
                    j -= 1
                else:
                    j += 1
                    break
            others = up(matrix, i-1, j)
            res.extend(others)
            return res

        return right(matrix, 0, 0)

class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []
        left, right, top, bottom = 0, n -1, 0, m -1
        while left <= right and top <= bottom:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1    
            
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                for i in range(right, left -1, -1):
                    res.append(matrix[bottom][i])
            bottom -= 1

            if left <= right:
                for i in range(bottom, top -1, -1):
                    res.append(matrix[i][left])
            left += 1
        return res



if __name__ == "__main__":
    print(Solution().spiralOrder([[1,2,3]]))
    print(Solution().spiralOrder([[1],[2],[3]]))
    print(Solution().spiralOrder([[2,5],[8,4],[0,-1]]))
    print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))