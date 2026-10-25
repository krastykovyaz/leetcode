# Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations

# LRUCache(int capacity) Initialize the LRU cache of size capacity.
# int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
# A key is considered used if a get or a put operation is called on it.

# Ensure that get and put each run in O(1) average time complexity.

# Example 1:

# Input:
["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]

# Output:
# [null, null, 10, null, null, 20, -1]

# Explanation:
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 10);  // cache: {1=10}
# lRUCache.get(1);      // return 10
# lRUCache.put(2, 20);  // cache: {1=10, 2=20}
# lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
# lRUCache.get(2);      // returns 20 
# lRUCache.get(1);      // return -1 (not found)

# ["LRUCache", [2], "put", [1, 1], "put", [2, 2], "get", [1], "put", [3, 3], "get", [2], "put", [4, 4], "get", [1], "get", [3], "get", [4]]

class Node:
    def __init__(self,key ,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.right = Node(0,0)
        self.left = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node):
        A, nxt = node.prev, node.next
        A.next = nxt
        nxt.prev = A

    def _insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
        node = Node(key, value)
        self._insert(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]
        
 

def print_lru(state):
    out = {}
    for k, v in state.items():
        out[k] = v.val
    return out

if __name__=='__main__':
    lru = LRUCache(2)
    print_lru(lru.cache)
    lru.put(1, 10)
    # print_lru(lru.cache)
    print(lru.get(1))
    # print_lru(lru.cache)
    lru.put(2, 20)
    # print_lru(lru.cache)
    lru.put(3, 30)
    # print_lru(lru.cache)
    print(lru.get(2))
    # print_lru(lru.cache)
    print(lru.get(1))
    # print_lru(lru.cache)
    # lru = LRUCache(2)
    # lru.put(1, 1)
    # lru.put(2, 2)
    # print_lru(lru.cache)
    # print(lru.get(1))
    # print_lru(lru.cache)
    # lru.put(3, 3)
    # print_lru(lru.cache)
    # print(lru.get(2))


