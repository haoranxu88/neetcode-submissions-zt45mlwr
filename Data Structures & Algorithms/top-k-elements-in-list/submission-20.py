class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # map frequency to list of numbers
        freqs = defaultdict(int)
        for n in nums:
            freqs[n] += 1
        freq_to_nums = defaultdict(list)
        for n, v in freqs.items():
            freq_to_nums[v].append(n)
        fs = sorted(freq_to_nums.keys())
        res = []
        for n in reversed(fs):
            curr = freq_to_nums[n]
            for x in curr:
                res.append(x)
                k -= 1
                if k <= 0:
                    return res
        return res


        