# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
#
# Given the root to a binary tree, count the number of unival subtrees.
#


#   0
#  /  \
# 1    0
#    /  \
#   1    0
#  / \  / \
# 1   1 0  0
#      /
#     0


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def unival_subtree_count(rt):

    if not rt.left and not rt.right:
        Node.unival += 1
    elif rt.left and rt.right and rt.left.data == rt.right.data:
        Node.unival += 1
    elif (rt.left and not rt.right and rt.data == rt.left.data) or \
            (rt.right and not rt.left and rt.data == rt.right.data):
        Node.unival += 1
    if rt and rt.left:
        unival_subtree_count(rt.left)
    if rt and rt.right:
        unival_subtree_count(rt.right)
    return Node.unival


# create nodes
root = Node('0')
n1 = Node('1')
n2 = Node('0')
n3 = Node('1')
n4 = Node('0')
n5 = Node('1')
n6 = Node('1')
n7 = Node('0')
n8 = Node('0')
n9 = Node('0')


# setup children
root.left = n1
root.right = n2
n2.left = n3
n2.right = n4
n3.left = n5
n3.right = n6
n4.left = n7
n4.right = n8
n8.left = n9


Node.unival = 0


print("Number of unival trees: ", unival_subtree_count(root))
