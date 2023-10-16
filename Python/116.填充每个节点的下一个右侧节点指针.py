#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#
from typing import Optional

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
    
    def __str__(self) -> str:
        return f"{self.val}"
    
    def __repr__(self) -> str:
        return self.__str__()
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        nodes = [root]
        index = 1
        i = 0
        pre = None
        while nodes:
            node = nodes.pop(0)
            i += 1
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
            if pre:
                pre.next = node
            pre = node
            if i >= index:
                index = index * 2
                i = 0
                pre = None
        return root



# @lc code=end
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(Solution().connect(root))
