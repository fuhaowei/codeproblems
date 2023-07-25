dp all about optimization problems, shortest path, or best ways to do something
-> kind of a exhaustive search, usually that's a bad thing bcs it's exponential time
    -> but DP makes it polynomial time

dp = CAREFUL BRUTE FORCE!
dp = take a problem, solve subproblems, then reuse in subproblems
dp = 

1. memoization

    -> if something i calculated before already, don't do it again. don't do it again, then this reduces time and maybe space complexity as well.

    -> for the 2d array walking through, we are breaking down the problem into one where it's reduced into how many ways you can travel from top left to bottom right of that size of the grid
    
    -> u realize u r always breaking down the problem into something smaller, and calculations are repeated, so u know what can be memoized liao from there


    template:

    def memoize(f):
        memo = {}
        memo base cases
        def helper(x):

            if x in memo:
                return memo[x]
            else:
                #the helper(x) below is the recurisve call ya. the new thing
                memo[x] = helper(x-1)
                return memo[x]

        return helper(f)



    let's say given target sum, array of stuff, then we wanna figure out if we can get target sum.

    



2. tabulation


 