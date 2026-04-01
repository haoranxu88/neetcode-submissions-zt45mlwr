class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        for n in nums:
            hm[n] += 1
        arr = []
        for n, c in hm.items():
            arr.append([c, n])
        arr.sort()
        res = []
        for i in range(k):
            res.append(arr.pop()[1])
        return res

        
            

        
        