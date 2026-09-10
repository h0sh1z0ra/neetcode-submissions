class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(arr, n, i):
            # root
            largest = i

            # left index = 2i+1
            l = 2*i + 1
            # right index = 2i+2
            r = 2*i + 2

            # if left child larger than root
            if l < n and arr[l] > arr[largest]:
                largest = l
            # if right child larger than root
            if r < n and arr[r] > arr[largest]:
                largest = r
            
            # if largest is not root
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        def heapSort(arr):
            n = len(arr)

            for i in range(n//2, -1, -1):
                heapify(arr, n, i)
            
            # for each element in heap
            for i in range(n-1, 0, -1):
                # move root to end
                arr[0], arr[i] = arr[i], arr[0]
                heapify(arr, i, 0)
        
            return arr
        
        return heapSort(nums)