# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        res = []
        queue = []
        queue.append(root)
        num_left = len(queue)

        while bool(queue):
            curr = queue.pop(0)

            num_left -= 1
            if num_left == 0:
                res.append(curr.val)

            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)

            if num_left == 0:
                num_left = len(queue)

        return res