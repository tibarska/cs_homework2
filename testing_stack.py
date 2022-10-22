import unittest
from stack import Stack


class TestStack(unittest.TestCase):

    def testing_push(self):
        pass

    def testing_pop(self):
        stack = Stack()
        val = stack.pop()
        self.assertTrue(val is None)

if __name__ == '__main__':
    unittest.main()
