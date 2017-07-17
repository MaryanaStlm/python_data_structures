from stack import Stack
import unittest

class TestMyStack(unittest.TestCase):

    def test_init(self):
        empty_stack = Stack()
        filled_stack = Stack([1, 2, 3])

        self.assertEqual(empty_stack.get_items(), [])
        self.assertEqual(empty_stack.size(), 0)

        self.assertEqual(filled_stack.get_items(), [1, 2, 3])
        self.assertEqual(filled_stack.size(), 3)

    def test_is_empty(self):
        empty_stack = Stack()
        filled_stack = Stack([1, 2, 3])

        self.assertTrue(empty_stack.isEmpty())
        self.assertFalse(filled_stack.isEmpty())

    def test_push(self):
        stack = Stack()

        for i in range(10):
            stack.push(i)

        self.assertEqual(stack.get_items(), [0,1,2,3,4,5,6,7,8,9])
        self.assertEqual(stack.size(), 10)

    '''

    def test_peek(self):
        self.assertEqual(s.peek(), 1)

    def test_stack_size(self):
        self.assertEqual(s.size(), 1)

    def test_pop(self):
        self.assertEqual(s.pop(), 3)
    '''
	
if __name__ == '__main__':
    unittest.main()
