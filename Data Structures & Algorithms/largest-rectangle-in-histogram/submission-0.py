class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # have a starting index and keep a running integer of max area.
        # push to the stack with index and height.
        # while the stack isn't empty, pop the index and height: find the maximum area, and change the starting index to be the index you popped
        # Keep a running count of the tallest height's index
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: # height of top greater than the height in the heights array
                idx, height = stack.pop()
                maxArea = max(maxArea, height * (i - idx))
                start = idx
            stack.append((start, h))
        
        # Horizontal mfs
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea