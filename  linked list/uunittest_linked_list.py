from newnode import Node
from newnode import LinkedList
import unittest

class TestMyLinkedList(unittest.TestCase):

    def test_node_init(self):
        node1 = Node(1)
        node2 = Node(2)
        node1.next = node2

        self.assertEqual(node1.next.get_data(), 2)

    def test_get_length(self):
        l1 = LinkedList()
        l2 = LinkedList()
        l2.push_back(1)

        self.assertEqual(l1.get_length(), 0)
        self.assertEqual(l2.get_length(), 1)

    def test_is_empty(self):
        l1 = LinkedList()
        l2 = LinkedList()
        l2.push_back('1')

        self.assertTrue(l1.is_empty())
        self.assertFalse(l2.is_empty())

    def test_is_contain(self):
        ll = LinkedList()
        ll.push_back(1)

        self.assertTrue(ll.is_contain(1))
        self.assertFalse(ll.is_contain(2))

    def test_push_front(self):
        ll = LinkedList()
        ll.push_front(1)
        ll.push_front(2)

        self.assertEqual(ll.get_items(), [2, 1])

    def test_push_back(self):
        ll = LinkedList()
        ll.push_back(1)
        ll.push_back(2)

        self.assertEqual(ll.get_items(), [1, 2])

    def test_insert(self):
        ll = LinkedList()
        ll.push_back(1)
        ll.push_back(2)
        ll.push_front(3)
        ll.insert(1, 4)

        self.assertEqual(ll.get_items(), [3, 4, 1, 2])

    def test_pop_front(self):
        ll = LinkedList()
        for i in range(3):
            ll.push_back(i)
        ll.pop_front()

        self.assertEqual(ll.get_items(), [1, 2])

    def test_pop_back(self):
        ll = LinkedList()
        for i in range(5):
            ll.push_back(i)
        ll.pop_back()

        self.assertEqual(ll.get_items(), [0, 1, 2 ,3])

    def test_remove_by_index(self):
        ll = LinkedList()
        for i in range(5):
            ll.push_back(i)
        ll.remove_by_index(2)

        self.assertEqual(ll.get_items(), [0, 1, 3, 4])

    def test_reverse(self):
        l1 = LinkedList()
        for i in range(5):
            l1.push_back(i)
        l1.reverse()

        self.assertEqual(l1.get_items(), [4, 3, 2, 1, 0])

        l2 = LinkedList()
        l2.push_back(2)
        l2.reverse()

        self.assertEqual(l2.get_items(), [2])

        l3 = LinkedList()
        for i in range(2):
            l3.push_back(i)
        l3.reverse()

        self.assertEqual(l3.get_items(), [1, 0])

    def test_equal(self):
        l1 = LinkedList()
        l2 = LinkedList()
        l3 = LinkedList()

        for i in range(5):
            l1.push_back(i)
            l2.push_back(i)

        for i in range(2, 7):
            l3.push_back(i)

        self.assertTrue(l1 == l2)
        self.assertFalse(l1 == l3)



if __name__ == '__main__':
    unittest.main()

