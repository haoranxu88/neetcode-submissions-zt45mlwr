class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # iterate through points and calculate distance from origin
        # store in min heap of distance, points
        minheap = []
        res = []
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(minheap, (dist, [x, y]))
        for i in range(k):
            res.append(heapq.heappop(minheap)[1])
        return res