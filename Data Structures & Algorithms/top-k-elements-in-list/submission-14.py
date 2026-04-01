class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freqs = defaultdict(int)
        for n in nums:
            freqs[n] -= 1
        for n, f in freqs.items():
            heapq.heappush(heap, (f, n))
        res = []
        for x in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

