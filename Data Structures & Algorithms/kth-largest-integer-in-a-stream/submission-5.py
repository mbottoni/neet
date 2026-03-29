class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = self.build_heap(nums)
        self.k = k
        while len(self.heap) > k:
            self.remove_min()                              # renamed
        
    def heapify_up(self, heap, index):
        parent = (index - 1)// 2
        while index>0 and index<len(heap) and heap[index] < heap[parent]:  # < instead of >
            heap[parent], heap[index] = heap[index], heap[parent]
            index = parent
            parent = (index - 1)// 2
        return heap
        
    def build_heap(self, nums):
        a = []
        for i in range(len(nums)):
            a.append(nums[i])
            self.heapify_up(a, len(a)-1)
        return a

    def remove_min(self):                                  # renamed
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)

    def heapify_down(self, index):
        n = len(self.heap)
        while True:
            smallest = index                               # renamed
            l, r = 2*index+1, 2*index+2
            if l < n and self.heap[l] < self.heap[smallest]: smallest = l  # < instead of >
            if r < n and self.heap[r] < self.heap[smallest]: smallest = r  # < instead of >
            if smallest == index: break
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

    def add(self, val: int) -> int:
        self.heap.append(val)
        self.heapify_up(self.heap, len(self.heap)-1)
        if len(self.heap) > self.k:
            self.remove_min()                              # renamed
        return self.heap[0]