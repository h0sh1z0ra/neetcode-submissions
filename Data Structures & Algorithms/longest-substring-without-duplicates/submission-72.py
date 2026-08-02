class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        # tmp_str = s[0:1]
        charSet = set()
        maxLen = 0

        if len(s) in (0,1):
            return len(s)

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.discard(s[l])
                l += 1
            
            charSet.add(s[r])
            maxLen = max(r - l + 1, maxLen)
        
        return maxLen
                