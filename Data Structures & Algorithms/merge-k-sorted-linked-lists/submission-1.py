# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        start = ListNode()
        curr = start
        while heap:
            value, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, i, node))

        return start.next