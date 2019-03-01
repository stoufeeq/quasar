#Linked List

class Node(object):
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

class LL(object):
    def __init__(self):
        self.headval = None

list1 = LL()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list1.headval.nextval = e2
e2.nextval = e3


print(list1.headval.dataval, list1.headval.nextval.dataval)