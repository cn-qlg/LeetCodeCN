#
# @lc app=leetcode.cn id=2265 lang=python3
#
# [2265] 统计值等于子树平均值的节点数
#
from typing import Optional
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        tc, s ,c = self.traverse(root, 0, 0, 0)
        # s += root.val
        # tc += 1
        # if s//tc == root.val:
        #     return c + 1
        return c

    def traverse(self, root: Optional[TreeNode], n, s, c):
        if not root:
            return n, s, c
        ltc, ls, lc = self.traverse(root.left, n, s, c)
        rtc, rs, rc = self.traverse(root.right, n, s, c)
        tc = ltc + rtc + 1
        s = ls + rs + root.val
        if s // tc == root.val:
            return tc, s, lc + rc + 1
        else:
            return tc, s, lc + rc

# @lc code=end

