class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        length, maxLen = 0, 0

        for num in numSet:
            if num - 1 not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                
            maxLen = max(maxLen, length)
            length = 0
        
        return maxLen