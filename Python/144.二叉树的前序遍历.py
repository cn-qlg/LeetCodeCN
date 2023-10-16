#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         """递归方法"""
#         return self.traversal(root, [])

#     def traversal(self, root: TreeNode, res: List[int]):
#         if not root:
#             return res
#         res.append(root.val)
#         res = self.traversal(root.left, res)
#         res = self.traversal(root.right, res)
#         return res

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """迭代方式"""
        if not root:
            return []
        nodes = []
        res = []
        while root or nodes:
            while root:
                res.append(root.val)
                nodes.append(root)
                root = root.left
            root = nodes.pop()
            root = root.right
        
        return res

# @lc code=end
