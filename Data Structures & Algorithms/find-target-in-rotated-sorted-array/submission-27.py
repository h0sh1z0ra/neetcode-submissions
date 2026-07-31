class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0; r = len(nums) - 1

        while l <= r:
            mid = (l+r)//2

            if target == nums[mid]:
                return mid

            # Pivot not in left half, and left half is sorted
            if nums[l] <= nums[mid]:
                # Must be outside the sorted left half
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                # Target is in sorted left half
                else:
                    r = mid - 1

            # Pivot is in left half, right half is sorted
            else:
                # Must be inside left half
                if target < nums[mid] or target > nums[r]:
                # if 6 is mid [3,5,6,0,1,2], and target is less than 6
                # and/or greater than 2, then it must be in the left half
                    r = mid - 1
    
                else:
                    l = mid + 1
            
        return -1
        