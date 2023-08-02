#key thought process here right -> 
#we store state for smaller amounts of money,
#just indexed in an array.
#follow the recursion -> if we return stuff, 
#we need to process the return codes at each
#stack of recursion. that makes sense?

#follow up -> if i needed one set of possible solution
#create another array, then when iterating through each coin
#if i use that coin, and the number of coins at that point
#is less than current value, then update both the minim vaue, and then
#the array[x] with the val of current coin

#After this calculation is done for all amounts up to n, the first array will store the first coin used to form each amount up to n.

#then to output optimal set, just trace downwrads

#this is only one solution, but if i wanted all

#computationally intensive, need explore all paths
#so we go onto recursively backtracking! see, makes sense



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
        