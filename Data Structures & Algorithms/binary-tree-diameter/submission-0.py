# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return -1

            leftHeight = dfs(root.left) + 1
            rightHeight = dfs(root.right) + 1
            currMaxHeight = max(leftHeight, rightHeight)
            currDiameter = leftHeight + rightHeight
            if currDiameter > self.res:
                self.res = currDiameter
            return currMaxHeight

        dfs(root)

        return self.res