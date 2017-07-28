class Node(object):

    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return str(self.data)

    def get_data(self):
        return self.data

    def print_list(node):
        while node:
            print(node.get_data())
            node = node.next