import heapq 
class Solution:
    def lastStoneWeight(self, stones):
        max_heap = []
        # Step 1: build heap
        for i in stones:
            heapq.heappush(max_heap, -i)
        # Step 2: smash until 1 or 0 left
        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)
            if x != y:
                heapq.heappush(max_heap, -(x - y))
        return -max_heap[0] if max_heap else 0