# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if not n:
            return []
        
        def helper(s, e):
            if s > e:
                return [None,]
            res = []
            for i in range(s, e+1):
                left_tree = helper(s, i-1)
                right_tree = helper(i+1, e)
                for l in left_tree:
                    for r in right_tree:
                        new_node = TreeNode(i)
                        new_node.left = l
                        new_node.right = r
                        res.append(new_node)
            return res
        return helper(1, n)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if not n:
            return []
        """
        For each node pick a unique node
        res = []
        
        i = 1
        
        left = []
        right = [2, 3]
        
        i = 2
        left = [1]
        right = [3]
        
        i = 3
        left = [1, 2]
        right = []
        
        need recursion
        base case: if not left and not right:
            return
        """
        def generate_trees(start, end):
            if start > end:
                return [None,]
            all_trees = []
            for i in range(start, end+1):
                left_trees = generate_trees(start, i-1)
                right_trees = generate_trees(i+1, end)
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
            return all_trees
            
        return generate_trees(1, n)
    """
    generate_trees(1, 3)
    start = 1
    end = 3
    
    all_trees = []
    
    i = 1
    left_trees = [None]
    right_trees = generate_trees(2, 3) = [None]
    
    
    right_trees = generate_trees(2, 3)
    start = 2
    end = 3
    all_trees = []
    i = 2
    left_trees = [None]
    right_tress = generate_trees(3, 3) = [None]
    
    right_trees = generate_trees(2, 3)
    start = 2
    end = 3
    all_trees = []
    i = 3
    left_trees = 
    right_tress = generate_trees(3, 3) = [None]
    
    
    
    
    
    
    right_tress = generate_trees(3, 3) = [None]
    start = 3
    end = 3
    all_tress = []
    i = 3
    left_trees = [None]
    right_tress = [None]
    """
        
        