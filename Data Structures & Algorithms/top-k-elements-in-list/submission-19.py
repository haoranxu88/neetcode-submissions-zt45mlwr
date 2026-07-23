class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        recounts = defaultdict(list)
        heap = []
        for n, v in counts.items():
            recounts[v].append(n)
        for c, ns in recounts.items():
            heapq.heappush(heap, -c)
        res = []
        while k > 0:
            v = -heapq.heappop(heap)
            for n in recounts[v]:
                res.append(n)
                k -= 1
        return res