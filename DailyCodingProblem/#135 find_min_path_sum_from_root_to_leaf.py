"""This question was asked by Apple.

Given a binary tree, find a minimum path sum from root to a leaf.
									 10
									 /  \
									5    5
									 \     \
									   2    1
										   /
										 -1
For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15. """

class Node:
	def __init__(self,val, left=None, right=None):
		self.val = val
		self.left = left
		self.right =right

root = Node(10,Node(5,None,Node(2)),Node(5,None,Node(1,Node(-1))))

def traverse(node):
	if node==None:
		return 0
	left = traverse(node.left)
	right = traverse(node.right)

	return node.val +min(left,right)

print(traverse(root))
