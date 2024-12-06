class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def addToHead(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.removeNode(node)
        self.addToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.removeNode(node)
            self.addToHead(node)
        else:
            node = Node(key, value)
            if len(self.cache) == self.capacity:
                lru = self.tail.prev
                self.removeNode(lru)
                del self.cache[lru.key]
            self.cache[key] = node
            self.addToHead(node)
