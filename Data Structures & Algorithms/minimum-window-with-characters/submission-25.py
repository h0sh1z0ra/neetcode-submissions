class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) <= len(t):
            if sorted(s) == sorted(t):
                return s
            else:
                return ""

        l = 0
        res, resLen = [-1,-1], 10**10   # hold pointers which have the shortest substring!!!
        counterS, counterT = Counter(), Counter()

        for c in t:
            counterT[c] = 1 + counterT.get(c, 0)
        
        have, need = 0, len(counterT)

        for r in range(len(s)):
            counterS[s[r]] = 1 + counterS.get(s[r], 0)

            if s[r] in counterT and counterS[s[r]] == counterT[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                # Shrink window; if it stops containing all the characters, decrement have
                counterS[s[l]] -= 1
                if s[l] in counterT and counterS[s[l]] < counterT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
                
        return s[l:r+1] if resLen != 10**10 else ""

