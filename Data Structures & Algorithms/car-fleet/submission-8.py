class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars  = [(pos, spd) for pos, spd in zip(position, speed)]
        cars.sort(reverse=True)   # "non-descending" order

        stack = []
        res   = 0

        for pos, spd in cars:
            stack.append((target-pos)/spd)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:  # less than or equal to time before it
                stack.pop()
            
            
        return len(stack)