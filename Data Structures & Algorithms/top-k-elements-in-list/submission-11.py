class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        l = 0

        while l < len(nums):
            seen[nums[l]] = 1 + seen.get(nums[l], 0)
        
            l+=1
        
        top_k = sorted(seen.items(), key=lambda x: x[1], reverse=True)[:k]

        return [key for key, val in top_k]