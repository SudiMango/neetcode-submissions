# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def is_same(r1: Optional[TreeNode], r2: Optional[TreeNode]):
            if r1 is None and r2 is None:
                return True
            elif r1 is None and r2 is not None:
                return False
            elif r1 is not None and r2 is None:
                return False
            elif r1 is not None and r2 is not None:
                if r1.val == r2.val:
                    return is_same(r1.left, r2.left) and is_same(r1.right, r2.right)
                else:
                    return False

        if root is None and subRoot is None:
            return True
        elif root is not None and subRoot is None:
            return True
        elif root is None and subRoot is not None:
            return False
        elif root is not None and subRoot is not None:
            same = is_same(root, subRoot)
            if not same:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            else:
                return True

        return False
