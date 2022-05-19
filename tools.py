from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)
    
    def __repr__(self) -> str:
        return self.__str__()


"""
先序遍历：DLR
中序遍历：LDR
后序遍历：LRD
"""


def generate_tree_1():
    """
        1
       / \
      2   2
     / \ / \
    3  4 4  3
    """
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(2)
    head.left.left = TreeNode(3)
    head.left.right = TreeNode(4)
    head.right.left = TreeNode(4)
    head.right.right = TreeNode(3)
    return head


def generate_tree_2():
    """
      1
     / \
    2   2
     \   \
     3    3
    """
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(2)
    head.left.right = TreeNode(3)
    head.right.right = TreeNode(3)
    return head


def generate_tree_3():
    """
    5
   / \
  4   1
   \   \
    1   4
   /   /
  2   2
  中序输出：N421N5N124N
    """
    head = TreeNode(5)
    head.left = TreeNode(4)
    head.right = TreeNode(1)
    head.left.right = TreeNode(1)
    head.left.right.left = TreeNode(2)
    head.right.right = TreeNode(4)
    head.right.right.left = TreeNode(2)
    return head


def generate_tree_4():
    """
    0
    """
    head = TreeNode(0)
    return head


def build_list(nodes: List[int]) -> ListNode:
    head = ListNode()
    p1 = head

    for v in nodes:
        node = ListNode(v)
        p1.next = node
        p1 = p1.next

    return head.next


def print_list_node(head: ListNode):
    values = []
    p = head
    while p:
        values.append(str(p.val))
        p = p.next
    print("->".join(values))
