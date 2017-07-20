from set import Set
import unittest

class TestMyStack(unittest.TestCase):

     def test_init(self):
         s = Set([1, 1, 2, 2])

         self.assertEqual(s.get_items(), [1, 2])

     #something strange
     def test_union(self):
         s1 = Set([1, 2, 3])
         s2 = Set([1, 4])
         s_union = s1 + s2

         self.assertEqual(s_union.get_items(), [1, 2, 3, 4])

     def test_intersection(self, other = []):
         s1 = Set([1, 2, 3])
         s2 = Set([1, 2])

         self.assertEqual(s1.intersection(s2), [1, 2])












if __name__ == '__main__':
    unittest.main()
