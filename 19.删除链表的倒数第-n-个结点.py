#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#
""" 
解题思路：
1. 先遍历总长度，然后第二遍遍历的是进行节点的删除。主要注意边界问题，第一个节点和最后一个节点。
2. 快慢指针，快指针比满指针多出n步。
3. 通过栈来进行操作。
"""
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self) -> str:
        return str(self.val)
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     cnt = 0
    #     h = head
    #     while h is not None:
    #         h = h.next
    #         cnt += 1
    #     if cnt == n:
    #         return head.next
    #     t = cnt - n -1
    #     p = head
    #     # print(cnt, t)
    #     while t > 0:
    #         p = p.next
    #         t -= 1
    #     # print(p.val)
    #     p.next = p.next.next

    #     return head 
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        q = head
        for _ in range(n):
            q = q.next
        if not q:
            return head.next
        while q.next:
            p = p.next
            q = q.next
        p.next = p.next.next
        return head
# @lc code=end
import tools
h = tools.build_list([1,2,3,4,5])
tools.print_list_node(h)
r = Solution().removeNthFromEnd(h, 1)
tools.print_list_node(r)

h = tools.build_list([1,2,3,4,5])
tools.print_list_node(h)
r = Solution().removeNthFromEnd(h, 2)
tools.print_list_node(r)

h = tools.build_list([1,2,3,4,5])
tools.print_list_node(h)
r = Solution().removeNthFromEnd(h, 3)
tools.print_list_node(r)

h = tools.build_list([1,2,3,4,5])
tools.print_list_node(h)
r = Solution().removeNthFromEnd(h, 4)
tools.print_list_node(r)

h = tools.build_list([1,2,3,4,5])
tools.print_list_node(h)
r = Solution().removeNthFromEnd(h, 5)
tools.print_list_node(r)

