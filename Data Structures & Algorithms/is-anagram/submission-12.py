class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charS, charT = {}, {}

        for char in s:
            charS[char] = 1 + charS.get(char, 0)
        
        for char in t:
            charT[char] = 1 + charT.get(char, 0)

        return charS == charT