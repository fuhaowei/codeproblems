# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#in order traversal recursive, just kth element. esm
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        #in order traversal, then pick

        sortedOrder = []

        def helper(node):

            if node.left:
                helper(node.left)

            sortedOrder.append(node.val)

            if node.right:
                helper(node.right)


        helper(root)
        print(sortedOrder)

        return sortedOrder[k-1]

