#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = head
        while p and p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head
    # def deleteDuplicates(self, head: ListNode) -> ListNode:
    #     if not head or not head.next:
    #         return head
    #     h = head        
    #     p = h.next
    #     h.next = None
    #     while p:
    #         if p.val != h.val:
    #             h.next = ListNode(p.val)
    #             h = h.next
    #         p = p.next
    #     return head


# @lc code=end
def print_list_node(head):
    while head:
        print(head.val, end='->')
        head = head.next
    print("")


def generate_list_node(values):
    h = p = ListNode(-1)
    for v in values:
        p.next = ListNode(v)
        p = p.next
    return h.next

print_list_node(Solution().deleteDuplicates(generate_list_node([1, 1])))
print_list_node(Solution().deleteDuplicates(generate_list_node([1, 1, 2])))
print_list_node(Solution().deleteDuplicates(
    generate_list_node([1, 1, 2, 3, 3])))
print_list_node(Solution().deleteDuplicates(
    generate_list_node([1, 1, 2, 3, 3, 3, 3, 4])))
