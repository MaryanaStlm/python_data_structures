class Node:
    def __init__(self, contents=None, next=None):
        self.__contents = contents
        self.next  = next

    def getContents(self):
        return self.__contents

    def __str__(self):
        return str(self.__contents)

def print_list(node):
    while node:
        print(node.getContents())
        node = node.next


'''node1 = Node("1")
node2 = Node("2")
node3 = Node("3")
node1.next = node2
node2.next = node3'''






