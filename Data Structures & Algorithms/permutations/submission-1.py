class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result=[]

        def backtrack(index, path):
            # 1. Check for doneness; base case
            if index == n:
                result.append(path[:])
                return
            
            # 2. Decisions; add a number at each node
            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack(index+1, path)
                    path.pop()

        backtrack(0, [])
        return result
            