class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        count = 0
        s = s[::-1]
        for i,char in enumerate(s):
            if i != 0 and lookup[s[i]] < lookup[s[i-1]]:
                count -= lookup[s[i]]
            else:
                count += lookup[char]
        return count