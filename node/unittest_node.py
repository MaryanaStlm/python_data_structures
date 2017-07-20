from node import Node
import unittest

class TestMyStack(unittest.TestCase):

    def test_init(self):
        node1 = Node("1")
        node2 = Node("2")
        node3 = Node("3")
        node1.next = node2
        node2.next = node3

        self.assertEqual(node1.next.getContents(), "2")
        self.assertEqual(node2.next.getContents(), "3")


if __name__ == '__main__':
    unittest.main()