class Solution:
    def climbStairs(self, n: int) -> int:


        #memotable is how many ways at that point

        memotable = {}
        

        def recurse(i):
            if i == 1:
                return 1

            if i == 2:
                return 2
 
            if i in memotable:
                return memotable[i]

            else:
                memotable[i] = recurse(i - 1) + recurse(i - 2)
                return memotable[i]


        return recurse(n)

            

            
