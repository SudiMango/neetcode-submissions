# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(node: Optional[TreeNode], low: int, high: int) -> bool:
            if node is None:
                return True
            
            if node.val > low and node.val < high:

                return helper(node.left, low, node.val) and helper(node.right, node.val, high)
            else:
                return False
        
        return helper(root, -1001, 1001)