# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = [root]
        while stack:
            node = stack.pop()
            # if node:
            # 	print(node.val)
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
        return root


s = Solution()
''' 
     4
   /   \
  2     7
 / \   / \
1   3 6   9
'''
node = TreeNode(4)
node.left = TreeNode(2)
node.right = TreeNode(7)
node.left.left = TreeNode(1)
node.left.right = TreeNode(3)
node.right.right= TreeNode(9)
node.right.left = TreeNode(6)
s.invertTree(node)