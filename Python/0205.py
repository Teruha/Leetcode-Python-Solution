# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        remaining = l1.val+l2.val
        head = ListNode(remaining%10)
        node = head
        remaining = remaining//10
        while l1.next or l2.next:
            l1 = l1.next or ListNode(0)
            l2 = l2.next or ListNode(0)
            remaining += l1.val+l2.val
            node.next = ListNode(remaining%10)
            node = node.next
            remaining = remaining//10
        if remaining:
            node.next = ListNode(remaining)
        return head

