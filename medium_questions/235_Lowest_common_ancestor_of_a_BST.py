# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Do a dfs on the tree 
If cur node > min(p, q) < max(p, q)
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur

        # Recursive
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Value of current node or parent node.
        parent_val = root.val

        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # If both p and q are greater than parent
        if p_val > parent_val and q_val > parent_val:    
            return self.lowestCommonAncestor(root.right, p, q)
        # If both p and q are lesser than parent
        elif p_val < parent_val and q_val < parent_val:    
            return self.lowestCommonAncestor(root.left, p, q)
        # We have found the split point, i.e. the LCA node.
        else:
            return root



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Need to find node where val is >= min(pVal, qVal) and <= max(pVal, qVal)

        if both greater than go right

        if both less go left
        """
        pVal, qVal = max(p.val, q.val), min(p.val, q.val)

        while True:
            if pVal >= root.val and qVal <= root.val:
                break
            
            if pVal < root.val and qVal < root.val:
                root = root.left
            else:
                root = root.right

        return root


        
        self.res = None

        pVal, qVal = max(p.val, q.val), min(p.val, q.val)

        def helper(node):
            if not node:
                return

            if pVal >= node.val and qVal <= node.val:
                self.res = node
                return
            
            if pVal < node.val and qVal < node.val:
                helper(node.left)
            else:
                helper(node.right)
        
        helper(root)
        return self.res


            
            
