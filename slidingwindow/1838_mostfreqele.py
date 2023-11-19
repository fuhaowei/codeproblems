#some things to consider -> the optimal target will always already exist in the array

#k-1 or k +1 will always lead to a less optimal result

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        nums.sort()

        ans = -1
        left = 0
        right = 0
        curr = 0

        #shrink the size of the left window

        while right < len(nums):
            #current target = nums[right]
            target = nums[right]
            curr += target

            #when expand too much, condition is wrong
            while (right-left + 1) * target - k > curr:
                curr -= nums[left]
                left += 1

            ans = max(ans, right-left + 1)

            right += 1

        return ans

        