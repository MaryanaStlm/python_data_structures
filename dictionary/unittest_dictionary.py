from dictionary import Dictionary
import unittest

class TestMyDictionary(unittest.TestCase):

    def test_init(self):
        d1 = Dictionary()
        self.assertEqual(d1.items(), [])

        d2 = Dictionary([(1, 'first'), (2, 'second')])
        self.assertEqual(d2.items(), [(1, 'first'), (2, 'second')])

        #how to test exception

    def test_keys(self):
        d1 = Dictionary()
        self.assertEqual(d1.keys(), [])

        d2 = Dictionary([(1, 'first'), (2, 'second')])
        self.assertEqual(d2.keys(), [1, 2])

    def test_values(self):
        d1 = Dictionary()
        self.assertEqual(d1.values(), [])

        d2 = Dictionary([(1, 'first'), (2, 'second')])
        self.assertEqual(d2.values(), ['first', 'second'])

    def test_update(self):
        d1 = Dictionary([(1, 'first'), (2, 'second')])
        d1.update(3, 'third')
        self.assertEqual(d1.items(), [(1, 'first'), (2, 'second'), (3, 'third')])

    def test_get(self):
        d1 = Dictionary([(1, 'first'), (2, 'second'), (3, 'third')])

        self.assertEqual(d1.get(1), 'first')
        self.assertEqual(d1.get(3), 'third')

    def test_set_default(self):
        d1 = Dictionary([(1, 'first'), (2, 'second'), (3, 'third')])

        self.assertEqual(d1.setdefault(3), 'third')

        d1.setdefault(4)
        self.assertEqual(d1.items(), [(1, 'first'), (2, 'second'), (3, 'third'), (4, None)])

    def test_pop(self):
        d1 = Dictionary([(1, 'first'), (2, 'second'), (3, 'third')])

        self.assertEqual(d1.pop(1), 'first')
        self.assertEqual(d1.pop(3), 'third')

    def test_getitem(self):
        d1 = Dictionary([(1, 'first'), (2, 'second'), (3, 'third')])

        self.assertEqual(d1[2], 'second')
        self.assertEqual(d1[3], 'third')

    def test_setitem(self):
        d1 = Dictionary([(1, 'first'), (2, 'second'), (3, 'third')])
        d1[4] = 'fourth'

        self.assertEqual(d1.items(), [(1, 'first'), (2, 'second'), (3, 'third'), (4, 'fourth')])

        d1[1] = 'one'
        self.assertEqual(d1.items(),  [(2, 'second'), (3, 'third'), (4, 'fourth'), (1, 'one')])






if __name__ == '__main__':
    unittest.main()
