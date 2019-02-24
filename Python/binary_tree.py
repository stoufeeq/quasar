# binary tree


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


#     A
#    / \
#   B   C
#  / \
# D   E

# create nodes
root = Node('A')
n1 = Node('B')
n2 = Node('C')
n3 = Node('D')
n4 = Node('E')

# setup children
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4


def pre_order(root1, nodes):
    nodes.append(root1.data)
    if root and root1.left:
        pre_order(root1.left, nodes)
    if root and root1.right:
        pre_order(root1.right, nodes)
    return nodes


def in_order(root1, nodes):
    if root1 and root1.left:
        in_order(root1.left, nodes)
    nodes.append(root1.data)
    if root1 and root1.right:
        in_order(root1.right, nodes)
    return nodes


def post_order(root1, nodes):
    if root1 and root1.left:
        post_order(root1.left, nodes)
    if root1 and root1.right:
        post_order(root1.right, nodes)
    nodes.append(root1.data)
    return nodes


def level_order(root1, nodes):
    queue = [root1]
    while queue:
        n = queue.pop(0)
        nodes.append(n.data)
        if n.left:
            queue.append(n.left)
        if n.right:
            queue.append(n.right)
    return nodes


print("pre_order traversal: ", pre_order(root, []))

print("in_order traversal: ", in_order(root, []))

print("post_order traversal", post_order(root, []))

print("level_order traversal", level_order(root, []))