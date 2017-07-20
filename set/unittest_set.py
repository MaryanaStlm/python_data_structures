from set import Set
import unittest

class TestMyStack(unittest.TestCase):

     def test_init(self):
         s = Set([1, 1, 2, 2])

         self.assertEqual(s.get_items(), [1, 2])

     def test_union(self, other = []):
         s1 = Set([1, 2, 3])
         s2 = Set([1, 4])
         s_union = s1 + s2

         self.assertEqual(s_union.get_items(), [1, 2, 3, 4])

     def test_intersection(self, other = []):
         s1 = Set([1, 2, 3])
         s2 = Set([1, 2])

         self.assertEqual(s1.intersection(s2).get_items(), [1, 2])

     def test_difference(self, other = []):
         s1 = Set(['m', 'y', 'e'])
         s2 = Set(['m', 'e'])

         self.assertEqual(s1.difference(s2).get_items(), ['y'])

     def test_is_subse(self, other = []):
         s1 = Set([11, 3, 21])
         s2 = Set([21, 3])

         self.assertTrue(s2.is_subset(s1))
         self.assertFalse(s1.is_subset(s2))












if __name__ == '__main__':
    unittest.main()
