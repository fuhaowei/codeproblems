# the point is - when we draw the recursion tree, dupes happen when we choose to include one element(2 for example). that branch of the tree is supposed to contain all the subsets
# regarding the element 2 correct. however, when the next element is the same, like 2, then
# if we choose that it would literally be repeating the subset
# so we must skip it until we get something we dk!
# and hence we need to skip all the dupes, but by iterating we cannot be sure, hence we must sort first

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        cur = []
        nums.sort()

        def backtrack(i):
            if i >= len(nums):
                res.append(cur[:])
                return

            cur.append(nums[i])
            backtrack(i + 1)
            
            #we figure out all subsets that don't include this number.
            #the idea is that if the next number is the same, then this act of non picking will actually lead to the same thing being picked
            cur.pop()
            while (i + 1 < len(nums) and nums[i] == nums[i+1]):
                i += 1
            backtrack(i + 1)

        backtrack(0)
        return res
