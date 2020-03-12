"""
Hi, here's your problem today. This problem was recently asked by Google:

Given a binary tree, find and return the largest path from root to leaf.

"""

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def largest_path_sum(tree):
    max_list = []
    max_sum = [float('-inf')]

    def helper(node,curr_list):
        global max_list

        if node is None:
            return
        if node.left is None and node.right is None:
            if max_sum[0] < sum(curr_list)+node.value:
                max_list = curr_list[::] +[node.value]
                max_sum[0] = sum(curr_list)+node.value
        helper(node.left,curr_list+[node.value])
        helper(node.right,curr_list+[node.value])
        return max_list

    
    ans = helper(tree,[])
    return ans


tree = Node(1)
tree.left = Node(3)
tree.right = Node(2)
tree.right.left = Node(4)
tree.right.right = Node(11)
tree.left.right = Node(5)
#    1
#  /   \
# 3     2
#  \   /
#   5 4
print(largest_path_sum(tree))
# [1, 3, 5]