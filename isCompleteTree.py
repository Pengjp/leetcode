# isCompleteTree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return False
        from collections import deque 
        q = deque()
        q.append(root)
        
        while q[0]:
            node = q.popleft()
            q.append(node.left)
            q.append(node.right)
        while q and not q[0]:
            q.popleft()
        
        return len(q) == 0