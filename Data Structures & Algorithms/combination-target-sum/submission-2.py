class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def bt(index, cur, total):
            if total == target:
                res.append(cur[:])
                return
            
            # exit condition, bad combo
            if index >= len(nums) or total > target:
                return 
            
            cur.append(nums[index])
            bt(index, cur, total+nums[index])
            cur.pop()
            bt(index+1, cur, total)
        
        bt(0, [], 0)
        return res