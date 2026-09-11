class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pS, pT = 0, 0

        if s == "":
            return True


        while pT < len(t):
            if pS == len(s)-1:
                return True

            if t[pT] == s[pS]:
                pS += 1
            
            pT += 1

        return False