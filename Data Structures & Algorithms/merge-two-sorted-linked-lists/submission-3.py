# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        head = None
        merged = None
        curr1 = None
        curr2 = None
        if list1.val <= list2.val:
            merged = list1
            curr1 = list1.next
            curr2 = list2
            head = list1
        else:
            merged = list2
            curr1 = list1
            curr2 = list2.next
            head = list2
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                merged.next = curr1
                merged = merged.next
                curr1 = curr1.next
            else:
                merged.next = curr2
                merged = merged.next
                curr2 = curr2.next
        merged.next = curr1 or curr2
        return head