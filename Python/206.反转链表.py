#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        h1 = head
        head = head.next
        h1.next = None
        while head:
            p1 = head
            head = head.next
            p1.next = h1
            h1 = p1

        return h1

# @lc code=end


if __name__ == "__main__":
    from tools import build_list, print_list_node
    h = build_list([1,2,3,4,5])
    print_list_node(h)
    print_list_node(Solution().reverseList(h))
    
