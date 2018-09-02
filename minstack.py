#!/usr/bin/python3

import unittest

class TestMinStack(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.stack = MinStack()

    def test_pushpop(self):
        for i in range(10):
            TestMinStack.stack.push(i)
        for i in range(9, -1, -1):
            self.assertEqual(i, TestMinStack.stack.pop())
        return

    def test_pushpopmins(self):
        case = [5, 3, 4, 2, 1]
        for el in case:
            TestMinStack.stack.push(el)
        
        # Check validity of mins as we pop from stack
        for i in range(len(case)):
            self.assertEqual(min(case[0:len(case) - i]), TestMinStack.stack.peekmin())
            TestMinStack.stack.pop()
        return

class MinStack:
    ''' A stack which supports usual stack ops
    ((push, pop, peek, isempty))
    as well as min (getmin) in O(1) time. '''
    
    def __init__(self):
        self.stack = [] # Contains tuples of (value, currentmin) pairs
        return

    def __repr__(self):
        return self.stack

    def push(self, value):
        if not self.stack:
            self.stack.append((value, value))
        else:
            self.stack.append((value, min(value, self.stack[-1][1])))
        return
    
    def pop(self):
        if not self.stack:
            return None
        else:
            val = self.stack[-1][0]
            self.stack = self.stack[:-1] # redundant copy?
            return val

    def peek(self):
        if not self.stack:
            return None
        else: 
            return self.stack[-1][0]

    def peekmin(self):
        if not self.stack:
            return None
        else:
            return self.stack[-1][1]


if __name__ == "__main__":
    print("Hello world")
    unittest.main()


