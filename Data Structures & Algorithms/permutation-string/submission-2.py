class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0; r = len(s1)
        target = Counter(s1)
        currStr = Counter(s2[l:r]) # up to r-1
        
        while r < len(s2):
            if currStr == target:
                return True
            
            currStr[s2[l]] -= 1
            if currStr[s2[l]] == 0:
                del currStr[s2[l]]

            l += 1

            currStr[s2[r]] = 1 + currStr.get(s2[r], 0)
            r += 1
            
        return currStr == target