class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0; j = 1; k = len(nums) - 1
        
        while i < len(nums)-2:
            target = -1*nums[i]

            while j < k:
                if nums[j] + nums[k] == target:
                    if [nums[i], nums[j], nums[k]] not in res: 
                        res.append([nums[i], nums[j], nums[k]])
                    
                    j+=1

                elif nums[j] + nums[k] > target:
                    k -= 1

                else:
                    j += 1

            i+=1; j = i+1; k = len(nums)-1
        
        return res

        # [-4,-1,-1,0,1,2]