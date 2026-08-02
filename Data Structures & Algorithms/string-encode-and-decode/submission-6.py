class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            str_length = len(string)
            encoded += str(str_length) + "#" + string
        
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        l = 0

        while l < len(s):
            tmp_len = ""
            tmp_str = []

            # Read nums until delimiter
            while s[l] != "#":
                tmp_len += s[l]
                l+=1

            tmp_len = int(tmp_len)
            l+=1

            for char in s[l:(l+tmp_len)]:
                tmp_str.append(char)
            
            decoded.append("".join(tmp_str))
            l += tmp_len

            tmp_len = ""; tmp_str = []

        return decoded