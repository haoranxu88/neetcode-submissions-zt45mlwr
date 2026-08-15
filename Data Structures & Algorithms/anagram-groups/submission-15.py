class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashy = defaultdict(list)
        for s in strs:
            sor = ''.join(sorted(s))
            hashy[sor].append(s)
        return list(hashy.values())