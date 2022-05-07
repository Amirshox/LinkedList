import unittest

from main import Solution
from nodelist import LinkedList


class TestSolution(unittest.TestCase):

    def test_first(self):
        l1 = LinkedList()
        l1.insert(2)
        l1.insert(4)
        l1.insert(3)

        l2 = LinkedList()
        l2.insert(5)
        l2.insert(6)
        l2.insert(4)

        result = Solution().nodelist_to_number(l1.head, l2.head)
        self.assertEqual(result, 708)

    def test_second(self):
        l1 = LinkedList()
        l1.insert(0)

        l2 = LinkedList()
        l2.insert(0)

        result = Solution().nodelist_to_number(l1.head, l2.head)
        self.assertEqual(result, 0)

    def test_third(self):
        l1 = LinkedList()
        l1.insert(9)
        l1.insert(9)
        l1.insert(9)
        l1.insert(9)
        l1.insert(9)
        l1.insert(9)
        l1.insert(9)

        l2 = LinkedList()
        l2.insert(9)
        l2.insert(9)
        l2.insert(9)
        l2.insert(9)

        result = Solution().nodelist_to_number(l1.head, l2.head)
        self.assertEqual(result, 89990001)


if __name__ == '__main__':
    unittest.main()
