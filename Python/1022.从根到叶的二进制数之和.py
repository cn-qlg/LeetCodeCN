#
# @lc app=leetcode.cn id=1022 lang=python3
#
# [1022] 从根到叶的二进制数之和
#
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        sum = 0

        def traverse(root:TreeNode, path:List[int], sum)->int:
            path.append(root.val)
            if not root.left and not root.right:
                s  = binaryToInt(path)    
                return sum + s       
            if root.left:
                sum = traverse(root.left, path[:], sum)
            if root.right:
                sum = traverse(root.right, path[:], sum)
            return sum
        
        def binaryToInt(binaries:List[int]):
            s,c = 0, len(binaries)-1
            
            for bin in binaries:
                if bin == 1:
                    s += 2 ** c
                c -= 1
            return s
        
        return traverse(root, [], 0)
                

# @lc code=end
# def binaryToInt(binaries:List[int]):
#     s,c = 0, len(binaries)-1            
#     for bin in binaries:
#         if bin == 1:
#             s += 2 ** c
#         c -= 1
#     return s

# print(binaryToInt([1,0,0]))
# print(binaryToInt([1,0,1]))
# print(binaryToInt([1,1,1]))
r = TreeNode(1)
r.left = TreeNode(0)
r.right = TreeNode(1)
r.left.left = TreeNode(0)
r.left.right = TreeNode(1)
r.right.left = TreeNode(0)
r.right.right = TreeNode(1)
print(Solution().sumRootToLeaf(r))