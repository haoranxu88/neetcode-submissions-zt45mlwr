class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashes = {}
        for s in strs:
            hm = {}
            for i in s:
                if i in hm:
                    hm[i] += 1
                else:
                    hm[i] = 1
            key = tuple(sorted(hm.items()))
            if key in hashes:
                hashes[key].append(s)
            else:
                hashes[key] = [s]
        retlist = []
        for k, v in hashes.items():
            retlist.append(v)
        return retlist
