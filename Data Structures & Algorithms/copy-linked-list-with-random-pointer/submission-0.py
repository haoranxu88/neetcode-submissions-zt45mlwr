"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # since random can point to a previous pointer, we need to link every next node then connect randoms
        if not head:
            return None
        new_map = defaultdict(Node)
        new_map[head] = Node(head.val, head.next)
        curr = head
        while curr.next:
            curr = curr.next
            new_map[curr] = Node(curr.val)
        curr = head
        while curr:
            if curr.next:
                new_map[curr].next = new_map[curr.next]
            if curr.random:
                new_map[curr].random = new_map[curr.random]
            curr = curr.next
        return new_map[head]
            
