#bottom up, no need recursion


#dp general tips -> dp[i] if i'm dealing with generating some sequence, usually is up to that length
#if generating sequence, case to last thing in sequence [x] -> 2d dp right

#counting number of ways to do something is always dp of course

#

class Solution:
    def knightDialer(self, n: int) -> int:

    #top down dp 

    #recursive memoization thing is slower (like what i was thinking about caching)
    #advantage of this is for some problems u can return early
    #once you find any path from the final state i am looking for to the base case, it works/return true.
    #for bottom up i would need to compute everything then go all the way back up
    #this would be word break 

    #{square -> [wtv u can jump to]}

    #dp[i][x] represents the number of ways to make a number of length i if you end on x

    #[[0,1,2,3,4,5,6,7,8,9], [0,1,2,3,4,5,6,7,8,9]]

        dp = [[0] * 10 for j in range(n+1)]

        #0 indexed
        moves_array = [[4,6],[8, 6], [7, 9], [4,8], [0,3,9], [], [0, 1,7],[2,6], [1,3], [2,4]]

        for x in range(10):
            dp[1][x] = 1

        for i in range(1,n+1):
            for x in range(10):
                for possiblemoves in moves_array[x]:
                    dp[i][x] += dp[i-1][possiblemoves]
        print(dp)

        ans = sum(dp[-1]) % (10**9 + 7)
        return ans




