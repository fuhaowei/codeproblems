from collections import Counter

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        freqcount = Counter(nums)
  

        for key,v in freqcount.items():
        
            if v > 1:
                idxlist = []
                for idx in range(len(nums)):
                    if nums[idx] == key:
                        idxlist.append(idx)

                for i in range(len(idxlist)):
                    for j in range(i + 1, len(idxlist)):
                        if abs(idxlist[i] - idxlist[j]) <= k:
                            return True


        return False