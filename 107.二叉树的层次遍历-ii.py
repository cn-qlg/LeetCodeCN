#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List, Text
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        nodes = [root]
        values = [[root.val]]
        while True:
            c_nodes = []
            for node in nodes:                
                if node.left:
                    c_nodes.append(node.left)
                if node.right:
                    c_nodes.append(node.right)
            if not c_nodes:
                break
            nodes = c_nodes
            values.append([node.val for node in nodes])
        # print(values)
        return values[::-1]

# @lc code=end

