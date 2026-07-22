class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = range(len(nums)+1)
        pointer = 0

        while pointer < len(expected):
            if expected[pointer] not in nums:
                return expected[pointer]
            pointer+=1