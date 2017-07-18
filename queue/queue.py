import unittest 

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()
for i in range(10):
	q.enqueue(i)




class TestMyQueue(unittest.TestCase):
    unittest.TestCase
    '''
    def test_is_empty(self):
        self.assertTrue(q.isEmpty())'''

    def test_size(self):
        self.assertEqual(q.size(), 10)


    def test_dequeue(self):
        self.assertEqual(q.dequeue(), 0)



if __name__ == '__main__':
    unittest.main()
