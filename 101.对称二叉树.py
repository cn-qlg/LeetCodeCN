#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.is_child_nodes_symmetric(root.left, root.right)
    
    def is_child_nodes_symmetric(self, left: TreeNode, right: TreeNode):
        if left and not right:
            return False
        if not left and right:
            return False
        
        if not left and not right:
            return True
        if left.val != right.val:
            return False
        return self.is_child_nodes_symmetric(left.left, right.right) and self.is_child_nodes_symmetric(left.right, right.left)

    def isSymmetric_1(self, root: TreeNode) -> bool:
        # 迭代，广度优先，判断每一层是否对称。
        layer_nodes = [root]
        while layer_nodes:
            current_layer_nodes = []
            current_layer_values = []
            for node in layer_nodes:
                if node:
                    current_layer_nodes.append(node.left)
                    current_layer_nodes.append(node.right)
                    current_layer_values.append(node.val)
                else:
                    current_layer_values.append(None)
            # print(current_layer_values)
            if not self.is_layer_symmetric(current_layer_values):
                return False
            layer_nodes = current_layer_nodes
        return True
    
    def is_layer_symmetric(self, values):
        l = 0
        r = len(values) - 1
        while l < r:
            if values[l] != values[r]:
                return False
            else:
                l += 1
                r -= 1
        return True

    # def isSymmetric(self, root: TreeNode) -> bool:
    #     self.values = []
    #     self.traverse(root)
    #     l = 0
    #     r = len(self.values) - 1
    #     while l < r:
    #         if self.values[l] != self.values[r]:
    #             return False
    #         else:
    #             l += 1
    #             r -= 1
    #     return True

    # def traverse(self, node: TreeNode):
    #     if not node:
    #         return
    #     if not node.left and node.right:
    #         self.values.append(None)
    #     self.traverse(node.left)
    #     self.values.append(node.val)
    #     self.traverse(node.right)
    #     if node.left and not node.right:
    #         self.values.append(None)


# @lc code=end
from tools import generate_tree_1,generate_tree_2, generate_tree_3

print(Solution().isSymmetric(generate_tree_1()))
print(Solution().isSymmetric(generate_tree_2()))
print(Solution().isSymmetric(generate_tree_3()))
