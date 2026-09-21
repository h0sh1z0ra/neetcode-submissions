class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)

        # pop if it has more than k elements
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Executes if has less than k elements
        heapq.heappush(self.minHeap, val)

        # accounts for edge case where len < k
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        # smallest in the heap
        return self.minHeap[0]


