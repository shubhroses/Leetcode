# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        split in half
        if size of nums is 1 return node
        """
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        mid = len(nums)//2
        
        return TreeNode(nums[mid], self.sortedArrayToBST(nums[:mid]), self.sortedArrayToBST(nums[mid+1:]))