class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #Neet code solution
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
        
        
        
        #My solution
        if not root:
            return None
        if root == p or root == q:
            return root
        x, y = min(p.val, q.val), max(p.val, q.val)
        
        if root.val > x and root.val < y:
            return root 
        if root.left and root.val > x and root.val > y:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.right and root.val < x and root.val < y:
            return self.lowestCommonAncestor(root.right, p, q)