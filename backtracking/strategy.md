## Backtracking

hey, backtracking is just a selective tree/graph traversal method but with a stopping condition when we realize the path is not viable anymore.

Backtracking is an algorithmic paradigm that uses a depth-first search (DFS) strategy to try out solutions to subproblems, but whenever it determines that a proposed solution is not viable, it abandons the path and goes back (hence the name "backtracking") to explore the next path.

It's often used in problems where you need to find all possible combinations or permutations, such as the N-Queens problem, generating all possible subsets or permutations of a set, solving Sudoku, and so on. If you go down a path that you discover can't lead to a solution, you "backtrack" and try a different path.

So yes, you can think of backtracking as a version of DFS with the added step that if a path doesn't lead to a solution, it is abandoned and a different path is tried. It's essentially an optimization over naive DFS approach where you would explore all paths (even those that clearly won't lead to a solution) exhaustively.

```
def backtrack():
    if condition:  # Condition when we should stop our exploration.
        result.append(current[:])  # Append a copy of the current state to the result
        return
    for i in range(num, last + 1):
        current.append(i)  # Explore candidate.
        backtrack()  # Recursive call with updated 'current'
        current.pop()  # Abandon candidate.

```
Permutation: can be thought of number of ways to order some input.
Example: permutations of ABCD, taken 3 at a time (24 variants): ABC, ACB, BAC, BCA, ...
Combnation: can be thought as the number of ways of selecting from some input.
Example: combination of ABCD, taken 3 at a time (4 variants): ABC, ABD, ACD, and BCD.
Subset: can be thought as a selection of objects form the original set.
Example: subset of ABCD: 'A', 'B', 'C', 'D,' 'A,B' , 'A,C', 'A,D', 'B,C', 'B,D', 'C,D', 'A,B,C', ...
