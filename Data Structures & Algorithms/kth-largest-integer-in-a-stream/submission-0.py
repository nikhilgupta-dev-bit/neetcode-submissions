import heapq 
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # for the largest we need a min_heap 
        self.min_heap=[]
        self.k=k
        for i in nums:
            heapq.heappush(self.min_heap,i)
            if len(self.min_heap)>self.k:
                heapq.heappop(self.min_heap)
    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap,val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
        
