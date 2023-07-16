#rmbr not only need to check every step, need check  the bounds also. hold the bounds like 210

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def helper(node, lb, ub):
            if not node:
                return True

            if not lb < node.val < ub:
                return False


            if not helper(node.left, lb, node.val):
                return False

            if not helper(node.right, node.val, ub):
                return False

            return True



        return helper(root, float(-inf), float(inf))


            
            



