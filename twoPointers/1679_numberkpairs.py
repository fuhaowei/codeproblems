class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        nums.sort()
        lp = 0
        rp = len(nums) - 1
        ans = 0

        while lp < rp:
            if nums[lp] + nums[rp] == k:
                ans += 1
                lp += 1
                rp -= 1

            elif nums[lp] + nums[rp] < k:
                lp += 1

            else:
                rp -= 1

        return ans
