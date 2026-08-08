class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1; r = max(piles)
        bestSpeed = r

        while l <= r:
            mid = l + (r-l)//2

            # n log m cuz you still need to iterate through piles
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile/mid)

            if totalTime <= h:
                bestSpeed = mid
                r = mid-1
            
            else:
                l = mid+1
        
        return bestSpeed