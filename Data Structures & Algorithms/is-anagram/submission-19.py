class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charS, charT = {}, {}

        # for char in s:
        #     charS[char] = 1 + charS.get(char, 0)
        
        # for char in t:
        #     charT[char] = 1 + charT.get(char, 0)

        # for i in range(len(s)):
        #     charS[s[i]] = 1 + charS.get(s[i], 0)
        #     charT[t[i]] = 1 + charT.get(t[i], 0)f


        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False

        return True