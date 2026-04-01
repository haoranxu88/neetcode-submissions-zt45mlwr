class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''
        s_map = defaultdict(int)
        t_map = defaultdict(int)
        for char in t:
            t_map[char] += 1
        have, need = 0, len(t_map)
        l = 0
        res = [-1, -1]
        res_len = float('inf')
        for r in range(len(s)):
            s_map[s[r]] += 1
            if s[r] in t_map and s_map[s[r]] == t_map[s[r]]:
                have += 1
            while have == need:
                if (r - l + 1) < (res_len):
                    res = [l, r]
                    res_len = r - l + 1
                s_map[s[l]] -= 1
                if s[l] in t_map and s_map[s[l]] < t_map[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if res_len != float('inf') else ''

     
            