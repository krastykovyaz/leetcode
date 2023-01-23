from collections import OrderedDict

class LRUcache:
    def __init__(self, t: int) -> None:
        self.capacity = t
        self.cache = OrderedDict()

    def get(self, key: int)-> int:
        if key not in self.cache:
            return -1
        ans = self.cache[key]
        del self.cache[key]
        self.cache[key] = ans
        return ans

    def put(self, key: int, value: int)->None:
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = value
        while len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

if __name__=='__main__':
    obj = LRUcache(2)
    for item in [[2,1], [1,1],[2,3],[4,1]]:
        print(obj.cache)
        obj.put(item[0], item[1])
    print(obj.get(1))
    print(obj.get(2))

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__=='__main__':
    capacity = 2
    obj = LRUCache(capacity)
    obj.put(2, 1)
    obj.put(2, 2)
    # obj.put(3, 3)
    print(obj.get(2))
    obj.put(1, 1)
    print('cache', obj.cache_dict)
    obj.put(4, 1)
    print('cache', obj.cache_dict)
