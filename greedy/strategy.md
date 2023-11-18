With dynamic programming, at each step we make a choice which usually dependents on and by comparing between the multiple solutions of the recurrence relation. 

Greedy algorithm is way easier than that! We find a rule, sort the items by some type of ordering — time, distance, size, or some type of ration, and we construct our optimal solutions incrementally w/o considering preceding items or choices incrementally and we end up having our optimal solution. 


If we have multiple optimal solutions, usually greedy algorithm will only give us one! In dynamic programming, we solve subproblems before making the first choice and usually processing in a bottom-up fashion; a greedy algorithm makes its first choice before solving any subproblems, which is usually in top-down fashion, reducing each given problem instance to a smaller one.

## Due to the special relationship between greedy algorithm and the dynamic programming: ‘’beneath every greedy algorithm, there is almost always a more cumbersome dynamic programming solution”, we can try the following six steps to solve a problem which can be potentially solved by making greedy choice:

# greedy problems -> 

True/False
Maximum/Minimum number



## Algo to see if we can use greedy
Divide the problem into subproblems, including one small problem and the remaining subproblem.
Determine the optimal substructure of the problems (formulating a recurrence function).
Show that if we make the greedy choice, then only one subproblem remains.
Validate the rightness of the greedy choice.
Write either a recursive or an iterative implementation.


Pros:
Simplicity: Greedy algorithms are often easier to describe and code up than other algorithms.
Efficiency: Greedy algorithms can often be implemented more efficiently than other algorithms.
Cons:
Hard to design: Once you have found the right greedy approach, designing greedy algorithms can be easy. However, finding the right approach can be hard.
Hard to verify: Showing a greedy algorithm is correct often requires a nuanced argument.


## Types of Greedy Algorithm
Activity-Selection: given a set of activities with start and end time (s, e), our task is to schedule maximum non-overlapping activities or remove minimum number of intervals to get maximum non-overlapping intervals. In cases that each interval or activity has a cost, we might need to retreat to dynamic programming to solve it.

Frog Jumping: usually it is array. This normally corresponds with the coordinate type of dynamic programming problems.

Data Compression
File Merging
Graph Algorithms, such as Minimum Spanning Trees algorithms (prim and Kruskal), Minimum path (Dijkstra). For weighted graph that has negative values, we have to use dynamic programming, such as Bellman Ford algorithms.