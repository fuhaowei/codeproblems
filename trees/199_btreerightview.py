#literally bfs but at every level add the last element


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        queue = deque()

        ans= []

        queue.append(root)

        while queue:

            lenq = len(queue)
            temp = []

            for _ in range(lenq):
                top = queue.popleft()
                if top:
                    temp.append(top.val)
                    if top.left:
                        queue.append(top.left)
                    if top.right:
                     queue.append(top.right)

            ans.append(temp[-1])

        return ans