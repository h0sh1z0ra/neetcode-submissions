class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seen_s = {}; seen_t = {}

        for i in range(len(s)):
            seen_s[s[i]] = seen_s.get(s[i], 0) + 1
            seen_t[t[i]] = seen_t.get(t[i], 0) + 1

        if seen_s != seen_t:
            return False
        else:
            return True  