class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def heapify(arr, n, i):
            # largest as root
            largest = i

            # left index
            l = 2*i + 1
            # right index
            r = 2*i + 2

            # if left child larger than root
            if l < n and arr[l] > arr[largest]:
                largest = l
            # if right
            if r < n and arr[r] > arr[largest]:
                largest = r

            # if neither
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)
        
        def heapSort(arr):
            n = len(arr)

            for i in range(n//2, -1, -1):
                heapify(arr, n, i)
            
            for i in range(n-1, 0, -1):
                arr[0], arr[i] = arr[i], arr[0]
                heapify(arr, i, 0)
            
            return arr
        
        return heapSort(nums)