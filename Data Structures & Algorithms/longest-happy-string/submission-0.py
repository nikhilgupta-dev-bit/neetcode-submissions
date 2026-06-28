import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        # push negative counts for max heap behavior
        if a > 0:
            heapq.heappush(maxHeap, (-a, 'a'))
        if b > 0:
            heapq.heappush(maxHeap, (-b, 'b'))
        if c > 0:
            heapq.heappush(maxHeap, (-c, 'c'))
        s = ""

        while maxHeap:
            count, char = heapq.heappop(maxHeap)

            # if adding this char creates 3 consecutive
            if len(s) >= 2 and s[-1] == s[-2] == char:
                if not maxHeap:
                    break

                count2, char2 = heapq.heappop(maxHeap)
                s += char2
                count2 += 1  # since negative

                if count2 < 0:
                    heapq.heappush(maxHeap, (count2, char2))

                heapq.heappush(maxHeap, (count, char))

            else:
                s += char
                count += 1

                if count < 0:
                    heapq.heappush(maxHeap, (count, char))

        return s



        