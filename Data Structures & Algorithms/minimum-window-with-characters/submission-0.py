class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = {}
        for i in t:
            t_dict[i] = t_dict.get(i, 0) + 1
        window = {}
        l = 0
        res = [-1, -1]
        res_len = float('infinity')
        have, need = 0, len(t_dict)
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in t_dict and window[c] == t_dict[c]:
                have += 1
            while have == need:
                if (r - l + 1) < res_len:
                    res_len = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in t_dict and window[s[l]] < t_dict[s[l]]:
                    have -= 1
                l += 1
        a, b = res
        return s[a:b + 1] if res_len != float('infinity') else ""
            
                
            
            
