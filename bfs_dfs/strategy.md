Remember:

Possible DFS traversals (notice naming based on where root is):

1. left, right, root (postorder, root at the right)
2. left, root, right (in order, root in middle)
3. root, left right (preorder, root at the start. pre. )



## DFS:

1) iterative solution

a. push to stack
b. pop the top
c. retrieve unvisited neighbours of top, push to stack
d. repeat, 1,2,3 while the stack isn't empty


