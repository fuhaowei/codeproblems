"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


#follow up to doing this without a stack:
#recurse downwards i guess






class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        #impt things to take note 
            #nodes in child list should all be set to none
            #nodes in child list should point nxt and prev to each other

        #pre order tree traversal
        #we do dfs with stack

        #keep a stack do basically do dfs priortizing the child
        #init a prev node pointer that basically stores our head
        #iterating down with it


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

         


#recursive

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
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':;
        #takes in 2 pointers as input, returns pointer of tail in the flattened list
        def recur(prev, curr):
            
            if not curr:
                return prev

            curr.prev = prev
            prev.next = curr

            tempNext = curr.next
            tail = recur(curr, curr.child)
            curr.child = None
            return recur(tail, tempNext)

            #curr leads to sublist we want to faltten, prev leads to element 
            #that should precede c
            #recursive case

        if not head:
            return head

        pseudohead = Node(None,None, head, None)
        recur(pseudohead, head)

        head.prev = None 
        return head



        