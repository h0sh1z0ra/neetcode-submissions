class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1

        while l < r:
            # Checking if character is valid (i.e., not alphanumeric)
            while l < r and not self.alphaNum(s[l]):
                l+=1
            while r > l and not self.alphaNum(s[r]):
                r-=1
            # If, at any point, the pointers aren't equal, then break and 
            # return False immediately
            if s[l] != s[r]:
                return False
                break
            l += 1; r -= 1
        return True

    def alphaNum(self, char):
        return (ord('A') <= ord(char) <= ord('Z') or 
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))