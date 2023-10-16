#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.generate_sub_tree(0, mid-1, nums)
        root.right = self.generate_sub_tree(mid+1, len(nums)-1, nums)
        return root

    
    def generate_sub_tree(self, low, high, nums):
        if low > high:
            return None
        else:
            mid = (low + high)//2
            c_root = TreeNode(nums[mid])
            c_root.left = self.generate_sub_tree(low, mid-1, nums)
            c_root.right = self.generate_sub_tree(mid +1, high, nums)
            return c_root
# @lc code=end

