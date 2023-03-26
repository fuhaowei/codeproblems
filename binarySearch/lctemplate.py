import sys


# just open this 
# sys.stdin = open("file.in", 'r')
# sys.stdout = open("file.out", 'w')

input = lambda : sys.stdin.readline().strip()
#generator in python, iterable but lazy iterable, call next() to get next value
intput = lambda : map(int, input().split())


if __name__  == "__main__":
    s = input()

    # gives me back iterable, do tuple assignment on iterable, 
    N, = intput()
    x, y, z = intput()
    A = [ *intput() ]

    # 2d array
    B = [ [*intput()] for _ in range(N)]

# binary search (sorted array, find things in logn time)

# but also works on functions, if function is monotonically increasing or decreasing, then you can use binary search to find the answer

# find the smallest x such that f(x) >= k
# find the largest x such that f(x) <= k

#when they say returning the min smthing, or return the max smthing, think about can i do binary search. then think about if its monotonic or not.

#koko eating bananas
# https://leetcode.com/problems/koko-eating-bananas/
# decide if monotonic -> if u can eat all bananas in h hours, then u can eat all bananas in h+1 hours, so yes.
# if speed works, check lower, if speed works, check higher


#if questions is about minimum integer,
#mid -> do floor divide

#if questions is max integer
#do ceiling divide
#ceil div = lambda x, y: (x + y - 1) // y


#2d prefix sums
#what do u see when u look at the bounds?

#1x10*18

#have to binary search, gotta be binary search
#binary seach, dividing by 2

#1x10*7
#starting possible with near

#1x10*6
#nlogn

#1x10*3
#n^2


#prefix sum
# scan in 210
# if give me a range of left and right, then i just take the value of right index, and minux the value of (left index -1)


# N, M = input() 

#leetcode 778
#https://leetcode.com/problems/swim-in-rising-water/

# binary search on the answer