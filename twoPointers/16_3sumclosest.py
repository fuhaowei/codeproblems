#2 pointer solution -> extended into 3 pointer! works bcs monotonic so rmbr to sort at the start

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        # print(nums)
        mindiff = float(inf)
        ans = 0

        for first in range(len(nums)-2):
            leftp = first + 1
            rightp = len(nums) - 1

            while leftp < rightp:
                cursum = nums[first] + nums[leftp] + nums[rightp]
                # print(nums[first], nums[leftp], nums[rightp])
                tempdiff = abs(target - cursum)
                # print("this is tempdiff" + str(tempdiff))
                # print("this is min diff" + str(mindiff))
                if tempdiff < mindiff:
                    ans = cursum
                    mindiff = tempdiff
                    # print("this is ans" + str(ans))  
                if cursum < target:
                    leftp += 1
                elif cursum == target:
                    return cursum
                else:
                    rightp -= 1
        
        return ans