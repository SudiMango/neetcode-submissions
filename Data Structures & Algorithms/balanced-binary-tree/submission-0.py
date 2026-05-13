# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ret = True
        
        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return -1

            leftHeight = dfs(root.left) + 1
            rightHeight = dfs(root.right) + 1
            displacement = abs(leftHeight - rightHeight)
            print("val: " + str(root.val) + " | displacement: " + str(displacement))
            if displacement > 1:
                if self.ret == True:
                    self.ret = False
            maxHeight = max(leftHeight, rightHeight)
            return maxHeight

        dfs(root)

        return self.ret