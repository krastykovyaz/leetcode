class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        if capacity < 1:
            print('LRUCache capacity must be > 0')
            return None
        self.capacity = capacity
        self.size = 0
        self.node_map = {}
        self.head = None
        self.tail = None

    def use_node(self, node):
        if node is self.head:
            return

        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next
        if node is self.tail:
            self.tail = self.tail.prev

        self.head.prev = node
        node.next = self.head
        node.prev = None
        self.head = node

    def get(self, key):
        if key in self.node_map:
            self.use_node(self.node_map[key])
            return self.node_map[key].val
        else:
            return -1

    def put(self, key, value):
        if key in self.node_map:
            self.use_node(self.node_map[key])
            self.node_map[key].val = value
        else:
            node = Node(key, value)
            self.node_map[key] = node

            if self.size == 0:
                self.head = node
                self.tail = node

            if self.size < self.capacity:
                self.size += 1

            elif self.size == self.capacity:
                k = self.tail.key

                if self.size == 1:
                    self.head = node
                    self.tail = node
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
                del self.node_map[k]

            self.use_node(node)

if __name__=='__main__':
    s = LRUCache()
