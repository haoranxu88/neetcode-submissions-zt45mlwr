# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # iterate to end, track parents
        curr = head
        prevs = {}
        while curr.next:
            prevs[curr.next] = curr
            curr = curr.next
        while head != curr and head != prevs[curr]:
            temp = head.next
            head.next = curr
            prevs[curr].next = None
            curr.next = temp
            curr = prevs[curr]
            head = temp
        curr.next = None
        

