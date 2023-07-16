
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # dfs down nodes, keep track of max, if while dfs haven't hit max then alls good

        ans = [0]

        def dfs(node, maxv):
            
            if node.val >= maxv:
                ans[0] += 1
                if node.left:
                    dfs(node.left, node.val)
                if node.right:
                    dfs(node.right, node.val)

            else:
                if node.left:
                    dfs(node.left, maxv)
                if node.right:
                    dfs(node.right, maxv)


        dfs(root,root.val)

        return ans[0]

          
            
