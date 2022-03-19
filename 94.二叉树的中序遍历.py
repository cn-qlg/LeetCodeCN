#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
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
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []
#         return self.traversal(root, [])
        
#     def traversal(self, root:TreeNode, result:List[int]):
#         if root.left:
#             result = self.traversal(root.left, result)
#         result.append(root.val)
#         if root.right:
#             result = self.traversal(root.right, result)
#         return result

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        stack =[]
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result

        
# @lc code=end

"""
result = [1] stack = [2], root = 2
stack = [2,3] root = 3
result [1,3] stack =  [3]
"""