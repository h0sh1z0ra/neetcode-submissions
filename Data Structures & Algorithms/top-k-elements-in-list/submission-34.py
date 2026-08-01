class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = 0
        seen = {}
        freq = [[] for i in range(len(nums)+1)]
        res = []

        while l < len(nums):
            seen[nums[l]] = 1 + seen.get(nums[l], 0)
            l+=1
        
        # top_k = sorted(seen.items(), key=lambda x: x[1], reverse=True)[:k]
        for key, val in seen.items():
            freq[val].append(key)
            # Append to the empty list

        # Start from end of len(buckets), count down until 0
        r = len(freq)-1
        while True:
            if freq[r] != []:
                for num in freq[r]:
                    res.append(num)
                    if len(res) == k:
                        return res
            r-=1