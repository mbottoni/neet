class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        tmp = self.cache[key]
        del self.cache[key]
        self.put(key, tmp)
        return self.cache.get(key)

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            tmp = self.cache[key]
            del self.cache[key]
            self.cache[key] = tmp

        self.cache[key] = value
        if len(self.cache) > self.capacity:
            del self.cache[list(self.cache.keys())[0]]
        
