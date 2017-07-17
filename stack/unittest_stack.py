import stack
import unittest

s = Stack()
s.push(1)

class TestMyStack(unittest.TestCase):

	def test_stack_empty(self):
		self.assertEqual(s.peek(), 1)
		
class TestMyStack(unittest.TestCase):
    def test_peek(self):
        self.assertEqual(s.peek(), 1)

    def test_stack_size(self):
        self.assertEqual(s.size(), 1)

    def test_pop(self):
        self.assertEqual(s.pop(), 3)
	
if __name__ == '__main__':
    unittest.main()