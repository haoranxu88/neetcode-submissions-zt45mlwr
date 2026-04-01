class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        maxheap = []
        for weight in stones:
            heapq.heappush(maxheap, -weight)
        while len(maxheap) > 1:
            x = -heapq.heappop(maxheap)
            y = -heapq.heappop(maxheap)
            if x < y:
                ny = y - x
                heapq.heappush(maxheap, -ny)
            elif y < x:
                nx = x - y
                heapq.heappush(maxheap, -nx)
        if len(maxheap) == 0:
            return 0
        return -heapq.heappop(maxheap)