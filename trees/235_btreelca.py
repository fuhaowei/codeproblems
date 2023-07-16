class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root.val == p.val:
            return root
        
        if root.val == q.val:
            return root

        if ((p.val < root.val  and root.val < q.val) or (q.val < root.val  and root.val < p.val)):
            return root

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)