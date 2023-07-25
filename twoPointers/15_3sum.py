#rmbr list not hashable. why?
 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = []
        check = set()
        nums.sort()

        for idx1 in range(len(nums) - 2):
            lp = idx1 + 1
            rp = len(nums) -1
            while lp < rp:
                total = nums[idx1] + nums[lp] + nums[rp]
                if total == 0:
                    if ((nums[idx1], nums[lp], nums[rp])) not in check:
                        ans.append([nums[idx1],nums[lp],nums[rp]])
                        check.add((nums[idx1], nums[lp], nums[rp]))
                        lp += 1
                        rp -= 1
                    else:
                        lp += 1
                        rp -= 1

                elif total < 0:
                    lp += 1

                else:
                    rp -= 1

        return ans



        
