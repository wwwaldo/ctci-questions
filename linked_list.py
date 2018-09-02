#!/usr/bin/python3

import unittest

class testLinkedList(unittest.TestCase):
    
    def testInserts():
        
        self.assertequal(1, 1)
        return

    def testPalin():
        return

    def testPalin_two():
        return

class LinkedNode():
    ''' A simple linked list implementation. '''

    def __init__(self, value):
        self.value = value
        self.next = None
        return

    def __str__(self):
        s = ''
        sep = ', '

        curr = self
        while curr is not None:
            s += curr.value + sep
            curr = curr.next

        s = s[:len(s) - len(sep)] # slice out sep
        return '[' + s + ']'

    def append(self, value):
        t = LinkedNode(value)

        curr = self
        while curr.next is not None:
            curr = curr.next
        curr.next = t
        return

if __name__ == '__main__':
    print("Hello world!")
    unittest.main()
