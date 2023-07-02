class Solution:
    def findMin(self, nums) -> int:

        low, high = 0, len(nums) -1

        #been rotated, let's find out where to move
        while low <= high:

            #if array is not rotated, return min
            if nums[low] <= nums[high]:
                return nums[low]

            #else i'll take he mid
            mid = (low + high)//2 

            #
            if nums[low] > nums[mid]:
                high = mid
            else:
                low = mid + 1