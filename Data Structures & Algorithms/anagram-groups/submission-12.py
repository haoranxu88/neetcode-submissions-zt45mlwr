class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorted string as key in hashmap defaultdict to words
        hm = defaultdict(list)
        for word in strs:
            s = sorted(word)
            k = ''.join(s)
            hm[k].append(word)
        res = []
        for k, v in hm.items():
            res.append(v)
        return res
