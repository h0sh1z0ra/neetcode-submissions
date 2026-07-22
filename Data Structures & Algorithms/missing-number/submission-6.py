class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = range(len(nums)+1)

        return (sum(expected) - sum(nums))