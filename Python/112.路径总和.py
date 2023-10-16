#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        递归方法，主要注意节点的值可能为负值，所以必须得遍历完才行，不可以提前返回。
        """
        return self.traversal(root, 0, targetSum)

    def traversal(self, root: TreeNode, sum, target):
        if not root:
            return False
        cur = sum + root.val

        if cur == target:
            if not root.left and not root.right:
                return True
        return self.traversal(root.left, cur, target) or self.traversal(root.right, cur, target)

        # @lc code=end

if __name__ == "__main__":
    root = TreeNode(-2)
    root.right = TreeNode(-3)
    print(Solution().hasPathSum(root, -5))

    root = TreeNode(1)
    root.left = TreeNode(-2)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(-2)
    root.left.left = TreeNode(-1)

    print(Solution().hasPathSum(root, -1))

    """
        1
      /   \   
    -2    -3
   /  \   /  \
 1     3 -2  
 /
-1
    """