# codeproblems

Here a sample repository of the leetcode problems I have tackled, and my basic strategies towards being able to identify and categorise solutions into solving then.


## general python pointers:

To use, we assume that the file "file.in" contains two integers separated by whitespace.

```
import sys

sys.stdin = open("file.in", 'r')
sys.stdout = open("file.out", 'w')

# Define the input and intput functions
input = lambda: sys.stdin.readline().strip()
intput = lambda: map(int, input().split())

# Read two integers from input and compute their sum
a, b = intput()
sum = a + b

# Write the sum to output
print(sum) 

```

More examples on how to use

```
if __name__  == "__main__":

    #reads string from input function, assings to s
    s = input()

    # This line uses the intput function to read a single integer value from input.
    
    # The trailing comma after N is used to unpack the single element from the iterable returned by intput and assign it directly to the variable N.

    N, = intput()

    #this line uses the intput function to read three integer values from input, which are then unpacked and assigned to the variables x, y, and z respectively.
    x, y, z = intput()

    #Here, the intput function is used to read multiple integer values from input, and the resulting iterable is converted into a list using the [*iterable] syntax. The list is assigned to the variable A.
    A = [ *intput() ]

    # generating a 2d array
    B = [ [*intput()] for _ in range(N)]

```


## topics

1. Backtracking: Essentially a depth-first search (DFS) for all possible sequences of decisions. It follows each path as far as possible and when it hits an invalid solution or dead-end, it "backtracks" to a previous decision and tries another path. It can be exhaustive if all paths need to be searched, but can be stopped early if a suitable solution is found.

2. Greedy Algorithms: Yes, these algorithms make the choice that seems the best at the current moment, with the hope that these local optimum choices will lead to a global optimum. They don't always produce the most optimal overall solution, especially for problems where the globally optimal solution requires making a seemingly sub-optimal choice at some point.

3. Dynamic Programming (DP): Not just "fancy DFS". While it does use a depth-first style recursive search, it also breaks down the problem into smaller subproblems, solves each subproblem only once (unlike DFS), and stores their solutions in case the same subproblem comes up again. It combines the power of recursion and memoization or tabulation to solve problems. DP aims to find the globally optimal solution and is particularly effective for problems where the optimal solution to the larger problem depends on the optimal solutions to the smaller subproblems.

Greedy algorithms and dynamic programming are both powerful problem-solving strategies, but they're used in different kinds of problems.

Greedy algorithms work best in problems where "greedy choices" lead to globally optimal solutions. This property is known as optimal substructure. Essentially, making the best local choice at each decision point leads to the best global outcome. Some situations where this is the case include:

Interval Scheduling Problems: If you're trying to schedule the maximum number of non-overlapping tasks given start and end times, a greedy algorithm can accomplish this by always picking the task that ends the earliest.
Huffman Coding: This is a common algorithm in data compression where greedy algorithms are used to create an optimal prefix code, minimizing the total length of the code.
Prim's and Kruskal's Algorithms: These are used in graph theory to find a minimum spanning tree. Both are examples of greedy algorithms.
However, if making the best local decision doesn't always lead to the best global solution, greedy algorithms fall short. These situations are where dynamic programming can excel.

For instance, in the knapsack problem, where you're trying to maximize the total value of items you can carry without exceeding the weight limit, making the "greedy" choice (like always picking the item with the highest value or highest value-to-weight ratio) doesn't always lead to the best solution. Instead, a dynamic programming approach, which considers all possible combinations, would be a better strategy.

In summary, use greedy algorithms when the problem exhibits the property of optimal substructure (the global optimum can be reached by combining the local optimums). Otherwise, consider dynamic programming or another approach.e