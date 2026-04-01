class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            if x == y:
                continue
            elif x > y:
                x -= y
                heapq.heappush(stones, -x)
            else:
                y -= x
                heapq.heappush(stones, -y)
        return -stones[0] if stones else 0
