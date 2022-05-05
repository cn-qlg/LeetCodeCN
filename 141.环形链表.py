#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     if not head:
    #         return False
    #     p = head.next
    #     index_p = 1
    #     while p:
    #         p = p.next
    #         index_p += 1

    #         q = head
    #         index_q = 0
    #         while q!= p:
    #             q = q.next
    #             index_q += 1
    #         if index_p != index_q:
    #             print(index_p, p.val ,index_q, q.val)
    #             return True
            
    #     return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
        
        
# @lc code=end

