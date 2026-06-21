class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        for g in gifts:
            heapq.heappush(heap, -g)
        for s in range(k):
            top = -heapq.heappop(heap)
            root = int(top**(0.5))
            heapq.heappush(heap, -root)
        return -sum(heap)