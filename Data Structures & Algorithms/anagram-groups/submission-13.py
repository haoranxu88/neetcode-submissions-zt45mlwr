class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for s in strs:
            sorted_string = sorted(s)
            m[tuple(sorted_string)].append(s)
        res = []
        for k, v in m.items():
            res.append(v)
        return res