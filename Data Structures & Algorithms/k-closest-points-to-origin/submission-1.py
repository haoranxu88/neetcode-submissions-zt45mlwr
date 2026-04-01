class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        pts = defaultdict(list)
        for x, y in points:
            distance = (x**2 + y**2) ** (1/2)
            pts[distance].append([x, y])
            heapq.heappush(heap, distance)

        res = []
        while len(res) < k:
            d = heapq.heappop(heap)
            arr = pts[d]
            for p in arr:
                res.append(p)
        return res
