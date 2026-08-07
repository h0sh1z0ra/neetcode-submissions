class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = 0; r = (len(nums1)+len(nums2))-1
        nums = nums1+nums2
        nums.sort()

        mid = l + (r-l)//2

        if len(nums[:mid]) == len(nums[mid+1:]):
            return nums[mid]
        
        else:
            return (nums[mid]+nums[mid+1])/2