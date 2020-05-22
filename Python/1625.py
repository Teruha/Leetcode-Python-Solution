class LRUCache:
    
    def __init__(self, capacity: int):
        self.cache = collections.OrderedDict()
        self.cap = capacity

    def sortCache(self, target: List[List[int]]) -> None:
        target.sort(key = lambda x : x[2])


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)     #将当前key移到最后
        return self.cache[key]



    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(0)   #删除第一个元素





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)