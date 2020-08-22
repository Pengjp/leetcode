# Closest_Binary_Search_Tree_Value.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        res = root.val
        while root:
            if abs(root.val - target) < abs(res - target):
                res = root.val
            if target == root.val:
                return root.val
            if target > root.val:
                root = root.right
            else:
                root = root.left
        return res