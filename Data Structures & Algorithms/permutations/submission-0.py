class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result=[]

        def backtrack(path):
            # 1. Check for doneness; base case
            if len(path) == n:
                result.append(path[:])
                return
            
            # 2. Decisions; add a number at each node
            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack(path)
                    path.pop()

        backtrack([])
        return result
            