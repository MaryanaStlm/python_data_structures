from double_linked_list import DoublyLinkedNode
import unittest

class TestMyStack(unittest.TestCase):
    def test_init(self):
        node1 = DoublyLinkedNode('1')
        node2 = DoublyLinkedNode('2')
        node3 = DoublyLinkedNode('3')

        node1.next = node2
        node2.next = node3

        node2.prev = node1
        node3.prev = node2

        self.assertEqual(node1.next.get_contents(), '2')
        self.assertEqual(node2.prev.get_contents(), '1')



if __name__ == '__main__':
    unittest.main()