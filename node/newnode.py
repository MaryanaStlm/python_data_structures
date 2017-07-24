class Node(object):

    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

    def get_data(self):
        return self.data

    def __str__(self):
        return str(self.data)

    def print_list(node):
        while node:
            print(node.get_data())
            node = node.next

class LinkedList(object):

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def get_length(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def is_contain(self, item):
        node = self.head
        while node:
            if node.data == item:
                return True
            else:
                node = node.next
        return False

    def get_items(self):
        items = []
        node = self.head
        while node:
            items.append(node.data)
            node = node.next
        return items

    def push_front(self, data):
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head

    def push_back(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            iter_node = self.head
            while iter_node.next:
                iter_node = iter_node.next
            iter_node.next = new_node

    def insert(self, position, data):
        if position == 0 or not self.head:
            self.prepend(data)
        else:
            node_to_insert = Node(data)
            iter_node = self.head
            pos = position
            while pos>1 and iter_node.next:
                iter_node = iter_node.next
                pos-=1
            node_to_insert.next = iter_node.next
            iter_node.next = node_to_insert

    def pop_back(self):
        if not self.head:
            pass
        else:
            iter_node = self.head
            pos = self.get_length() - 1
            while pos > 1 and iter_node.next:
                iter_node = iter_node.next
                pos -=1
            if iter_node.next:
                iter_node.next = iter_node.next.next

    def pop_front(self):
        if not self.head:
            pass
        else:
            self.head = self.head.next

    def remove_by_index(self, position):
        if not self.head:
            pass
        else:
            iter_node = self.head
            pos = position
            while pos>1 and iter_node.next:
                iter_node = iter_node.next
                pos-=1
            if iter_node.next:
                iter_node.next = iter_node.next.next


    def reverse(self):
        if self.head:
            prev = None
            current = self.head
            while current:
                future = current.next
                current.next = prev
                prev = current
                current = future
            self.head = prev

    def list_print(self):
        node = self.head
        while node:
            print node.data
            node = node.next


