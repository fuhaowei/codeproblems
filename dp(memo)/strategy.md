dp: technique that combines the correctness of complete search with the efficiency of greedy algorithms

-> can be applied if problem can be divided into overlapping subproblems that can be solved independently

USE WHEN TRYING TO
1. Finding an optimal solution
2. Counting the number of solutions

-> kind of a exhaustive search, usually that's a bad thing bcs it's exponential time
    -> but DP makes it polynomial time

GREEDY DOES NOT GUARANTEE OPTIMAL, DP does

dp = CAREFUL BRUTE FORCE!
dp = take a problem, solve subproblems, then reuse in subproblems
dp = recursion where u cache the results!





### 5 type of problems of DP
1. 0/1 knapsack
2. unbounded knapsack
3. shortest paths (unique paths I/II)
4. fibonacci sequence (house thief, jump game)
5. longest common substring (longest palindromic substring, longest increasing subsequence)


## memoization

    -> if something i calculated before already, don't do it again. don't do it again, then this reduces time and maybe space complexity as well.

    -> for the 2d array walking through, we are breaking down the problem into one where it's reduced into how many ways you can travel from top left to bottom right of that size of the grid
    
    -> u realize u r always breaking down the problem into something smaller, and calculations are repeated, so u know what can be memoized liao from there

    -> make it work first! the naive recursion in a tree. can try testing with small one
    
    -> then memoize it and make it efficient by adding memo obj, add base case to return memo values, then store return values into memo


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



2. tabulation


 

## time and space analysis

-> base steps to think from -> naive fibo is f(n-1) and f(n-2)

-> rmbr 210 stuff -> the total number of nodes is the (numberofcalls)^n, where n stands for number of levels. time complexity is the number of nodes in the tree!
-> so most of the time, the time complexity is O(numberofcalls^n) 
-> for space complexity tho, rmbr it goes down all the way to the lowest level, then after that we return (pop off stack frame), then start new one. so maximum stack def is o(n)

-> so for fib(50), if naive it takes 2^50 steps which is crazy


-> so we can use memoization to reduce the time complexity to O(n) and space complexity to O(n) as well! 
-> space vs time trade off (classic)



# grid travelling
-> when i choose to move a certain way, u see that i'm actually shrinking the playable grid step by step, smaller and smaller, into some small case which we know!
-> try to represent in a tree -> smaller and smaller sections of the grid
-> number of levels is o(m + n), makes sense before u need get to the bototm
-> then space would be o(2^(m+n)) -> number of nodes in the tree

