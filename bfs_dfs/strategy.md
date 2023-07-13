Remember:

Possible DFS traversals (notice naming based on where root is):

1. left, right, root (postorder, root at the right)
2. left, root, right (in order, root in middle)
3. root, left right (preorder, root at the start. pre. )



### use stack for DFS (want to dive into the newly added stuff, so u r going down the tree in depth)

### use queue for BFS (u want to pick off the older stuff slowly, that's the level by level traversal)

## DFS:

1) iterative solution

a. push to stack
b. pop the top
c. retrieve unvisited neighbours of top, push to stack
d. repeat, 1,2,3 while the stack isn't empty




