class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        def bt(index, path):
            if index == n:
                result.append(path[:])
                return

            path.append(nums[index])
            bt(index+1, path)
            path.pop()
            bt(index+1, path)
        
        bt(0, [])
        return result