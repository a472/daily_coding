"""
Hi, here's your problem today. This problem was recently asked by Twitter:

Given a binary tree and an integer k, filter the binary tree such that its leaves don't contain the value k. Here are the rules:

- If a leaf node has a value of k, remove it.
- If a parent node has a value of k, and all of its children are removed, remove it.

			#     1												 #      1
			#    / \											 #	   /
			#   1   1        -----------filter(root,1)------->>>>#    1
			#  /   /											 #	 /
			# 2   1												 #  2
"""


class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __repr__(self):
		return f"value: {self.value}, left: ({self.left.__repr__()}), right: ({self.right.__repr__()})"


def filter(node, k):
	if node is None:
		return None
	node.right = filter(node.right, k)
	node.left = filter(node.left, k)

	if node.value == k and node.right is None and node.left is None:
		del node
		return None
	return node


n5 = Node(2)
n4 = Node(1)
n3 = Node(1, n4)
n2 = Node(1, n5)
n1 = Node(1, n2, n3)

print(filter(n1, 1))
