#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def removeElements(self, head: ListNode, val: int) -> ListNode:
#         while head and head.val == val:
#             head = head.next
#         if not head:
#             return head
#         p = head
#         q = head.next
#         while q:
#             if q.val == val:
#                 q = q.next
#             else:
#                 p.next = q
#                 p = p.next
#                 q = q.next
#         p.next = None
#         return head

# 优化版
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        h = ListNode()
        h.next = head
        p = h
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return h.next
# @lc code=end


if __name__ == "__main__":
    from tools import build_list
    nodes = build_list([1, 2, 6, 3, 4, 5, 6])
    Solution().removeElements(nodes, 6)
