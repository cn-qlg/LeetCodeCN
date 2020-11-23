#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        nodes = [root]
        depth = 0
        while True:
            layer_nodes = []
            if nodes:
                depth +=1
            for node in nodes:
                if node.left:
                    layer_nodes.append(node.left)
                if node.right:
                    layer_nodes.append(node.right)
            if not layer_nodes:
                break
            nodes = layer_nodes
        return depth

    # def maxDepth_1(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0
    #     return self.traverse(root, 0)

    # def traverse(self, node:TreeNode, depth):
    #     if not node:
    #         return depth
    #     else:
    #         return max(self.traverse(node.left, depth+1), self.traverse(node.right, depth+1))

# @lc code=end
from tools import generate_tree_1,generate_tree_2, generate_tree_3, generate_tree_4


print(Solution().maxDepth(generate_tree_1()))
print(Solution().maxDepth(generate_tree_2()))
print(Solution().maxDepth(generate_tree_3()))
print(Solution().maxDepth(generate_tree_4()))
print(Solution().maxDepth_1(generate_tree_1()))
print(Solution().maxDepth_1(generate_tree_2()))
print(Solution().maxDepth_1(generate_tree_3()))
print(Solution().maxDepth_1(generate_tree_4()))