class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair: (temp, idx)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, hottest_idx = stack.pop()
                res[hottest_idx] = i - hottest_idx
            
            stack.append((temp, i))
        
        return res
