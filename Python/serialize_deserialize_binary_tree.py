class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(rt, op):
    if rt is not None:
        op.append(rt.val)
        serialize(rt.left, op)
        serialize(rt.right, op)
    else:
        op.append('-1')
    return op


def deserialize_helper(arr):
    if not arr:
        return None
    nd = None
    value = arr.pop()
    if value != '-1':
        nd = Node(value)
        nd.left = deserialize_helper(arr)
        nd.right = deserialize_helper(arr)
    return nd


def deserialize(arr):
    arr.reverse()
    return deserialize_helper(arr)


node = Node('root', Node('left', Node('left.left', Node('left.left.left')), Node('left.right')),
            Node('right', Node('right.left'), Node('right.right')))

#                         ---------root--------
#                       /                       \
#                 ---left---                  --right--
#               /            \              /           \
#       left.left          left.right   right.left     right.right
#        /       \           /  \       /   \           /   \
# left.left.left   #        #   #       #   #           #   #
#    /       \
#   #        #
#
#   # signifies Null.

n = Node("7", Node("2", Node("1")), Node("5", Node("3"), Node("8")))


root = Node('7')
n1 = Node("2")
n2 = Node("1")
n3 = Node("5")
n4 = Node("3")
n5 = Node("8")


root.left = n1
root.right = n3
n1.left = n2
n3.left = n4
n3.right = n5


op = []
print(serialize(n, op))
op.clear()
print(serialize(root, op))
op.clear()
print(serialize(node, op))


my_arr = ['7', '2', '1', '-1', '-1', '-1', '5', '3', '-1', '-1', '8', '-1', '-1']

my_new_arr = ['root', 'left', 'left.left', 'left.left.left', '-1', '-1', '-1', 'left.right', '-1', '-1', 'right',
              'right.left', '-1', '-1', 'right.right', '-1', '-1']

rt = deserialize(my_new_arr)
print("root= ", rt.val, "\nrt.left=", rt.left.val, "\nrt.right=", rt.right.val, "\nrt.left.left= ", rt.left.left.val,
      "\nrt.right.left=", rt.right.left.val, "\nrt.right.right=", rt.right.right.val)

rt = deserialize(my_arr)
print("\nroot= ", rt.val, "\nrt.left=", rt.left.val, "\nrt.right=", rt.right.val, "\nrt.left.left= ", rt.left.left.val,
      "\nrt.right.left=", rt.right.left.val, "\nrt.right.right=", rt.right.right.val)