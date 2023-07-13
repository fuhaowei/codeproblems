# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack = []

        ans = []

        stack.append(root)


        #while stack has something in it, visit la.
        while stack:
            top = stack.pop()
            if top:
                if top.right:
                    stack.append(top.right)
                if top.left:
                    stack.append(top.left)
                ans.append(top.val)

        return ans
            