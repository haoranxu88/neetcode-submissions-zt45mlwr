import heapq
class MedianFinder:

    def __init__(self):
        self.left = [] # max heap
        self.right = [] # min heap

    def addNum(self, num: int) -> None:
        if not self.left or num <= -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        while len(self.left) - len(self.right) > 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        while len(self.right) - len(self.left) > 1:
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if (len(self.left) + len(self.right)) % 2 == 0:
            return float((-self.left[0] + self.right[0])) / 2
        else:
            return -self.left[0] if len(self.left) > len(self.right) else self.right[0]
        