#key thought process here right -> 
#we store state for smaller amounts of money,
#just indexed in an array.
#follow the recursion -> if we return stuff, 
#we need to process the return codes at each
#stack of recursion. that makes sense?

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #breaking down subproblem into smaller amounts of money basically

        dp = [-1] * (amount + 1)

        def recurse(i):
            #i is amount of money
            if i < 0:
                return -1

            if i == 0:
                return 0

            if dp[i] != -1:
                return dp[i]

            best = float('inf')
            for c in coins:
                trythis = recurse(i-c)
                if trythis != -1:
                    best = min(best, trythis + 1)

            dp[i] = best
            return best     

        ans = recurse(amount)     
        if ans == float('inf'):
            return -1
        else:
            return ans
        