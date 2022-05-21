#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#
""" 
解题思路：
1. 定义一个队列，用于存放即将需要着色的点。再定义一个集合，用于存放已经着色过的点。
对于队列中的每一个点，判断上下左右四个点是否满足要求，如果满足要求也未着色过，则添加到队列中。当队列为空的时候，停止循环。

1.1 优化。如果原色与目标色颜色相同，则不需要进行着色，可以直接返回。这样就不需要通过集合来去重了。
"""
from platform import node
from typing import List
# @lc code=start
class Solution:
    # def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    #     nodes = [(sr, sc)]
    #     oldColor = image[sr][sc]
    #     h = len(image)
    #     w = len(image[0])
    #     filledNodes = set()
    #     while nodes:
    #         i, j = nodes.pop()
    #         image[i][j] = newColor
    #         if i > 0 and image[i-1][j] == oldColor:
    #             if (i-1, j) not in filledNodes:
    #                 nodes.append((i-1, j))
    #                 filledNodes.add((i-1, j))
    #         if i < h -1 and image[i+1][j] == oldColor:
    #             if (i+1,j) not in filledNodes:
    #                 nodes.append((i+1,j))
    #                 filledNodes.add((i+1,j))
    #         if j > 0 and image[i][j-1] == oldColor:
    #             if (i, j-1) not in filledNodes:
    #                 nodes.append((i, j-1))
    #                 filledNodes.add((i, j-1))
    #         if j < w - 1 and image[i][j+1] == oldColor:
    #             if (i, j+1) not in filledNodes:
    #                 nodes.append((i, j+1))
    #                 filledNodes.add((i, j+1))
    #     return image
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        
        nodes = [(sr, sc)]

        h = len(image)
        w = len(image[0])
        while nodes:
            i, j = nodes.pop()
            image[i][j] = newColor
            if i > 0 and image[i-1][j] == oldColor:                
                nodes.append((i-1, j))                    
            if i < h -1 and image[i+1][j] == oldColor:                
                nodes.append((i+1,j))                    
            if j > 0 and image[i][j-1] == oldColor:                
                nodes.append((i, j-1))                    
            if j < w - 1 and image[i][j+1] == oldColor:                
                nodes.append((i, j+1))                    
        return image
            
# @lc code=end
print(Solution().floodFill([[0,0,0],[0,1,1]],1,1,1))
