# given 2 int lists A and B, same length N <= 1e5. where A[i] and B[i] <= 1e18

# choose a contiguous range of indices [L,R] such that for each i where L <= i <= R, 

# you must select either A[i] or B[i] (but not both). Then, putting ur selections together, 
#they must form a strictly increasing sequence.

# What's the maximum possible sum of such a selection?

#dp[i][j] = max sum of that if my sequence ends at j, i is A or B

#bottom up