class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        #dp array should represent at that point the LIS

        #subseq is not contiguous 

        dp = [1] * len(nums)


        for i in range(len(nums)):
            if i == 0:
                continue

            #compare to every single square before,
            #to see what's the longest possible one, checking all the prev squares
            else:
                for j in range(0,i):
                    if nums[i] > nums[j]:
                        dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)

