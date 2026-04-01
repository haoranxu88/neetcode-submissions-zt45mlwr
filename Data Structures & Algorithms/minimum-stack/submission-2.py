class Node:
    def __init__(self, val=None, mn=None, nxt=None, prev=None):
        self.val = val
        self.mn = mn
        self.nxt = nxt
        self.prev = prev

class MinStack:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.nxt = self.tail
        self.tail.prev = self.head
        self.size = 0

    def push(self, val: int) -> None:
        if self.size == 0 or val < self.tail.prev.mn:
            node = Node(val, val, self.tail, self.tail.prev)
        else:
            node = Node(val, self.tail.prev.mn, self.tail, self.tail.prev)
        self.tail.prev.nxt = node
        self.tail.prev = node
        self.size += 1

    def pop(self) -> None:
        if self.size == 0:
            return
        delete = self.tail.prev
        node = self.tail.prev.prev
        delete.prev = None
        delete.nxt = None
        node.nxt = self.tail
        self.tail.prev = node
        self.size -= 1


    def top(self) -> int:
        return self.tail.prev.val

    def getMin(self) -> int:
        return self.tail.prev.mn
