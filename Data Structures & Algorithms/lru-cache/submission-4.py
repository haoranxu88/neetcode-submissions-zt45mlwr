class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = capacity
        self.cache = {} # map key to nodes
        self.size = 0

    # remove from linked list
    def remove(self, node):
        del self.cache[node.key]
        last = node.prev
        after = node.next
        node.next = None
        node.prev = None
        last.next = after
        after.prev = last
        self.size -= 1

    # insert on the right
    def insert(self, node):
        self.cache[node.key] = node
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node
        self.size += 1

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        if self.size == self.cap:
            self.remove(self.head.next)
        self.insert(node)
        
