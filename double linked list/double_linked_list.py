class DoublyLinkedNode:
    def __init__(self, contents=None, prev = None, next=None):
        self.__contents = contents
        self.prev = prev
        self.next = next

    def get_contents(self):
        return self.__contents


node1 = DoublyLinkedNode('1')
node2 = DoublyLinkedNode('2')
node3 = DoublyLinkedNode('3')

node1.next = node2
node2.next = node3

node2.prev = node1
node3.prev = node2

print node1.next.get_contents()
print node2.prev.get_contents()