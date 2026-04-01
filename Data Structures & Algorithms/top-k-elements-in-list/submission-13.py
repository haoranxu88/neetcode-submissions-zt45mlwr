class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_len = 0
        counts = {}
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
            if counts[i] > max_len:
                max_len = counts[i]
        buckets = [[] for _ in range(max_len + 1)]
        for key, val in counts.items():
            buckets[val].append(key)
        k_freq = []
        count = 0
        for i in range(len(buckets) - 1, -1, -1):
            for j in buckets[i]:
                if count == k:
                    return k_freq
                k_freq.append(j)
                count += 1
        return k_freq
        
        