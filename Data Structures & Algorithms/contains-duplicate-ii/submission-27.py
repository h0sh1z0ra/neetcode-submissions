class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        window = {}

        for i,num in enumerate(nums):
            if num in window and abs(window[num] - i) <= k:
                return True
        
            window[num] = i

        return False