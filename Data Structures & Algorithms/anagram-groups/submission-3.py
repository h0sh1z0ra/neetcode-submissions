class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)  # normal dict, but if a key with no value
        # is appended it appends an empty list as the value

        for s in strs:
            # Build letter frequency holder
            count = [0]*26
            for c in s:
                # Set letter frequency as the canonical key
                count[ord(c) - ord('a')] += 1 # Returns char as a number from 
                # 0-25; increments that number (letter) + 1
            result[tuple(count)].append(s)
        return list(result.values())
                