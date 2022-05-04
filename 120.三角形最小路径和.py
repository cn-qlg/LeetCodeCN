#
# @lc app=leetcode.cn id=120 lang=python
#
# [120] 三角形最小路径和
#

# @lc code=start


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i, row in enumerate(triangle[1:]):
            columnCnt = len(row)
            for j, c in enumerate(row):
                if j == 0:
                    triangle[i+1][j] += triangle[i][j]
                elif j == columnCnt - 1:
                    triangle[i+1][j] += triangle[i][j-1]
                else:
                    triangle[i+1][j] += min(triangle[i][j-1], triangle[i][j])
                # print(triangle[i+1])

        res = triangle[-1][0]
        for c in triangle[-1]:
            if c < res:
                res = c
        return res
# @lc code=end
print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))