# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:


        if not root:
            return 0

        #idea is to dfs from root, see all possible paths
        answer = set()

        def dfs(node, sums):
            if not node.left and not node.right:
                answer.add (sums + node.val)

            else:
                if node.left:
                    dfs(node.left, sums+node.val)

                if node.right:
                    dfs(node.right, sums+node.val)


        dfs(root, 0)

        if targetSum in answer:
            return True

        else:
            return False