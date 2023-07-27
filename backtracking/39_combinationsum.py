#EPHIPHANY MOMENT -> YES, SINCE WE CAN CHOOSE UNLIMITED
#TIMES, THEN WHEN WE CHOOSE TO INCLUDE THE SAME NUMBER, WE HAVE TO KEEP OUR INDEX THE SAME!
#RMRBR THIS!

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        #condition to stop -> when it's bigger then target
        # at every level either include or don't include again, since
        #there's an unlimited number of times 

        res = []
        posans = []

        def backtrack(i):
            if sum(posans) == target:
                res.append(posans[:])
                return

            if i >= len(candidates) or sum(posans) > target:
                return

            #choose yes
            posans.append(candidates[i])
            backtrack(i)

            #choose no
            posans.pop()
            backtrack(i+1)

        backtrack(0)
        return res
            
