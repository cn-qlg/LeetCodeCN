#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#
""" 
解题思路：
1. 第一次遍历获取链表总长度，第二次遍历到一半即可直接返回
2. 通过快慢指针，快指针一次遍历两格，慢指针一次走一格
"""
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def middleNode(self, head: ListNode) -> ListNode:
    #     h = head
    #     cnt = 0
    #     while h is not None:
    #         h = h.next 
    #         cnt += 1
    #     mid = cnt //2
    #     p = head
    #     while mid > 0:
    #         p = p.next 
    #         mid -= 1
    #     return p
    def middleNode(self, head: ListNode) -> ListNode:
        p = head
        q = head
        while q is not None and q.next is not None:
            p = p.next
            q = q.next.next
        return p

# @lc code=end
import tools
h = tools.build_list([1,2,3,4,5,6])
tools.print_list_node(h)
r = Solution().middleNode(h)
tools.print_list_node(r)

h = tools.build_list([1,2,3,4,5])
tools.print_list_node(h)
r = Solution().middleNode(h)
tools.print_list_node(r)