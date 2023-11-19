from collections import Counter
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:

        freqcount = Counter(nums)
        vals = list(freqcount.keys())
        #[1,3,5]
        #add everything from top down to bottom

        vals.sort(reverse = True)

        total = 0
        cur = 0
        for i in range(0, len(vals)-1):
            cur += freqcount[vals[i]]
            total += cur

        return total
            
        