class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        res_idx = 0; tmp_prod = 1

        while res_idx < len(nums):
            for num in nums[0:res_idx] + nums[res_idx+1:]:
                if num == 0:
                    tmp_prod = 0
                    break
                else:
                    tmp_prod *= num
                    
            res.append(tmp_prod)
            tmp_prod = 1
            res_idx += 1
        
        return res