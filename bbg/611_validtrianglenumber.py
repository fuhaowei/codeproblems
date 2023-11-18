#impt thing that makes a valid triangle number
#is that the 2 shorter sides summed together is bigger than 
#the one side

#fix k (biggest one)
#2 pointer the rest (smaller)
#once you get bigger, you know everything from j -i is a pair

#we get o(n^2) tiem and o(n) space


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        ans = 0

        for k in range(2,len(nums)):
            lp = 0
            rp = k-1

            while lp < rp:
                #everything between these 2ranges should be
                #correct! cos sorted right. 
                if nums[lp] + nums[rp] > nums[k]:
                        #every pair from lp -> rp, fixing rp and increasing lp
                        #should be correct, cos u only increase
                        ans += (rp - lp)
                        rp -= 1

                else:
                    #not big enough
                    lp += 1

        return ans


        