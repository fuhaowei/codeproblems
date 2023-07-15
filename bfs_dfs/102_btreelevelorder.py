# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#things to take note -> using the length
#of the queue during the bfs to 
#basically cycle the stuff -> 
#think is quite fundamental in bfs

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque()

        if root != None:
            queue.append(root)


        ans = []


        while len(queue) != 0:

            thislevel = []

            #check out need clear how many nodes
            lenq = len(queue)


            for _ in range(lenq):
                top = queue.popleft()
                thislevel.append(top.val)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)

            ans.append(thislevel)

        return ans
        



