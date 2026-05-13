# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = []
        queue.append(root)
        curr_iteration_num = len(queue)
        curr_idx = 0
        res = []

        while bool(queue):
            curr = queue.pop(0)
            if curr.left != None:
                queue.append(curr.left)
            if curr.right != None:
                queue.append(curr.right)

            curr_iteration_num -= 1

            if len(res) == curr_idx:
                res.append([curr.val])
            else:
                res[curr_idx].append(curr.val)

            if curr_iteration_num == 0:
                curr_iteration_num = len(queue)
                curr_idx += 1

        return res