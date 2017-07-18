from queue import Queue
import unittest

class TestMyQueue(unittest.TestCase):

    def test_init(self):
        empty_q = Queue()
        filled_q = Queue([1, 2, 'Maryana'])

        self.assertEqual(empty_q.get_items(), [])
        self.assertEqual(filled_q.get_items(), [1, 2, 'Maryana'])

    def test_isEmpty(self):
        empty_q = Queue()
        filled_q = Queue([1])
        

        self.assertTrue(empty_q.isEmpty())
        self.assertFalse(filled_q.isEmpty())


    def test_enqueue(self):
        q = Queue([1])
        q.enqueue(2)

        self.assertEqual(q.size(), 2)

    def test_dequeue(self):
        q = Queue([1])
        q.dequeue()

        self.assertTrue(q.isEmpty())

    def test_size(self):
        empty_q = Queue()
        filled_q = Queue([1, 2, 3])

        self.assertEqual(empty_q.size(), 0)
        self.assertEqual(filled_q.size(), 3)


if __name__ == '__main__':
    unittest.main()

