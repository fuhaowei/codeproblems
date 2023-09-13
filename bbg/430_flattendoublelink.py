"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        #impt things to take note 
            #nodes in child list should all be set to none
            #nodes in child list should point nxt and prev to each other

        #pre order tree traversal
        #we do dfs with stack
        if not head:
            return None

        stack = [head]
        previousnode = None

        while stack:
            curr = stack.pop()
            if previousnode:
                previousnode.next = curr
                curr.prev = previousnode
                
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)

            curr.child = None

            previousnode = curr

        return head

         


            
         sm