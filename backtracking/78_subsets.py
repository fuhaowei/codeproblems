#dfs right -> but u choose at each level should i include or not

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        subset = []

        #i is the index of the thing we r currently choosing
        def backtrack(i):
            if i >= len(nums):
                res.append(subset[:])
                return 
            
            subset.append(nums[i])
            backtrack(i + 1)

            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return res
