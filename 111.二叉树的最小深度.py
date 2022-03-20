#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class IndexNode:
    def __init__(self, node, depth) -> None:
        self.node = node
        self.depth = depth
    
    def __str__(self) -> str:
        return f"IndexNode:{self.node.val}-{self.depth}"
    
    def __repr__(self) -> str:
        return self.__str__()


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """
        广度优先算法，依次将每个子节点都加入到队列中，并记录节点对应的深度。
        如果该节点无左右子节点，则说明是叶子节点，直接返回当前深度。
        """
        if not root:
            return 0
        nodes = [IndexNode(root, 1)]
        while nodes:
            iNode = nodes.pop(0)
            print(f"cur node:{iNode}")
            if not iNode.node.left and not iNode.node.right:
                print(iNode.depth, iNode.node.val)
                return iNode.depth
            if iNode.node.left:
                nodes.append(IndexNode(iNode.node.left, iNode.depth +1))
            if iNode.node.right:
                nodes.append(IndexNode(iNode.node.right, iNode.depth + 1))
            print(nodes)

# @lc code=end
