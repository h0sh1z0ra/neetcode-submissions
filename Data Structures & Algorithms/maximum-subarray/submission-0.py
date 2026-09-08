class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm
        maxSub, curSum = nums[0], 0
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)
        
        return maxSub