Remember:

Possible DFS traversals (notice naming based on where root is):

1. left, right, root (postorder, root at the right)
2. left, root, right (in order, root in middle)
3. root, left right (preorder, root at the start. pre. )



### use stack for DFS (want to dive into the newly added stuff, so u r going down the tree in depth)

### use queue for BFS (u want to pick off the older stuff slowly, that's the level by level traversal)

## DFS:

1.  iterative solution

a. push to stack
b. pop the top
c. retrieve unvisited neighbours of top, push to stack
d. repeat, 1,2,3 while the stack isn't empty

 
## BFS:

1. remember to cycle through the bfs using the length of the queue. outside while loop would be while the deque is not empty, inside a for loop with how many times you need to bfs each time.


2. usually the right thing for shortest path, not DFS

For graphs having unit edge distances, shortest paths from any point is just a BFS starting at that point, no need for Dijkstra’s algorithm.

Maze solving problems are mostly shortest path problems and every maze is just a fancy graph so you get the flow.






## graph stuff

1. union find algorithm:
    -> use to detect cycles in undirected graphs