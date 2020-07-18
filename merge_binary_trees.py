# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def Inorder(root):
	if root:
		Inorder(root.left)
		print(root.val)
		Inorder(root.right)

# t1
'''     1
	   / \
	  2   3
	 / \  /
	5  6 10
   /
  9   
'''		

t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)
t1.right.left = TreeNode(10)
t1.left.right = TreeNode(6)				
t1.left.left = TreeNode(5)
t1.left.left.left = TreeNode(9)

t2 = TreeNode(1)


def mergeTrees(t1 : TreeNode,t2 : TreeNode):
	# if both trees are empty return nothing
	if not t1 and not t2:
		return None

	if t1 and t2:
		ans = TreeNode(t1.val + t2.val)
	else: # if one of them is empty
		if not t1: # if t1 is empty
			ans = TreeNode(t2.val)
		else: # if t2 is empty 
			ans = TreeNode(t1.val)

	ans.left = mergeTrees(t1 and t1.left, t2 and t2.left)
	ans.right = mergeTrees(t1 and t1.right, t2 and t2.right)

	return ans

Inorder(mergeTrees(t1,t2))