class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack  = []  # (temp, idx)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, hottestIdx      = stack.pop()
                result[hottestIdx] += i - hottestIdx
            stack.append((temp, i))

        return result
