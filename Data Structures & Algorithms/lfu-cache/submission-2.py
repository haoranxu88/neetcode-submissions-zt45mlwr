class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.frequencies = {} # key : frequencies
        self.keytoval = {} # key : value (node pointer)
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.prev = self.tail, self.head

    # helper function for moving
    def move(self, node):
        curr = node
        while curr.next.next and curr.next.val != None and self.frequencies[curr.next.key] <= self.frequencies[curr.key]:
            b = node.next
            nextNode = b.next
            prevNode = curr.prev
            curr.next = nextNode
            nextNode.prev = curr
            b.next = curr
            curr.prev = b
            prevNode.next = b
            b.prev = prevNode

    # helper function for insert
    def insert(self, node):
        self.frequencies[node.key] = 1
        self.keytoval[node.key] = node
        nextNode = self.head.next
        self.head.next, node.prev = node, self.head
        nextNode.prev, node.next = node, nextNode
        self.size += 1

    # helper function for remove
    def remove(self):
        removeNode = self.head.next
        nextNode = removeNode.next
        del self.frequencies[removeNode.key]
        del self.keytoval[removeNode.key]
        nextNode.prev, self.head.next = self.head, nextNode
        self.size -= 1


    def get(self, key: int) -> int:
        if key in self.keytoval:
            self.frequencies[key] += 1
            self.move(self.keytoval[key])
            return self.keytoval[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # cases:
        # 1. if capacity full -> update, put (need to remove)
        # 2. if capacity not full -> update, put
        if self.size >= self.cap:
            if key in self.keytoval:
                self.keytoval[key].val = value
                self.frequencies[key] += 1
                self.move(self.keytoval[key])
            else:
                self.remove()
                newNode = Node(key, value)
                self.insert(newNode)
                self.move(newNode)
        elif self.size < self.cap:
            if key in self.keytoval:
                self.keytoval[key].val = value
                self.frequencies[key] += 1
                self.move(self.keytoval[key])
            else:
                newNode = Node(key, value)
                self.insert(newNode)
                self.move(newNode)

        
# head = least freq used, tail = most freq used
# hashmap of key : value (node pointer)
# size int, cap int
# hashmap of key : freq
# on each get or put, increment count of a node and move it rightward until either at tail
# or next node freq count > current node count (guarantees we remove correct node)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)