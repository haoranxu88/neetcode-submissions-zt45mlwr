# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        tail = head
        node_to_prev = {}
        while tail.next:
            node_to_prev[tail.next] = tail
            tail = tail.next
        while head != tail and head != node_to_prev[tail]:
            head_next = head.next
            head.next = tail
            node_to_prev[tail].next = None
            tail.next = head_next
            head = head_next
            tail = node_to_prev[tail]
