#!/usr/bin/python3

# all the linked list questions, and also an implementation
# move these out sometime later..

import unittest

class testLinkedList(unittest.TestCase):
    
    def testInserts(self):
        l = LinkedNode(0)
        
        for i in range(1, 10):
            l.append(i)
        
        self.assertEqual( str(l), str(list(range(10))) )
        return

    def testPalin(self): # not a palindrome
        vals = ['a', 'b', 'c']

        l = LinkedNode(vals[0])
        for val in vals[1:]:
            l.append(val)

        self.assertEqual( l.is_palindrome_runner(), False )
        return

    def testPalin_two(self): # even palindrome
        vals = 'abuttuba'
        l = LinkedNode(vals[0])
        for val in vals[1:]:
            l.append(val)
        self.assertEqual( l.is_palindrome_runner(), True )
        return

    def test_odd_palindrome(self):
        vals = 'abcdcba'
        l = LinkedNode(vals[0])
        for val in vals[1:]:
            l.append(val)
        self.assertEqual( l.is_palindrome_runner(), True )
        return

    def test_delete_interior(self):
        vals = 'abcdcba'
        l = LinkedNode(vals[0])
        for val in vals[1:]:
            l.append(val)

        test = l.next.next.next
        self.assertEqual( test.value, 'd' ) # sanity checking
        
        l.delete_interior(test)
        self.assertEqual("[a, b, c, c, b, a]", str(l) )

    def test_delete_duplicates(self):
        vals = 'ada'
        l = LinkedNode(vals[0])
        for val in vals[1:]:
            l.append(val)
        l.delete_duplicates()

        self.assertEqual("[a, d]", str(l) )

    def test_delete_duplicates_long(self):
        vals = 'abbb'
        l = LinkedNode(vals[0])
        for val in vals[1:]:
            l.append(val)
        l.delete_duplicates()

        self.assertEqual("[a, b]", str(l) )

class LinkedNode():
    ''' A linked list implementation with a slightly annoying api'''

    def __init__(self, value):
        self.value = value
        self.next = None
        return

    def __str__(self):
        s = ''
        sep = ', '

        curr = self
        while curr is not None:
            s += str(curr.value) + sep
            curr = curr.next

        s = s[:len(s) - len(sep)] # slice out sep
        return '[' + s + ']'
    
    # ---- some 'woah haskell'-type stuff ----
    
    # mimics accumulation over the linked list
    def _traverse(self, func, ivalue):
        curr = self
        accum = ivalue
        while curr is not None:
            accum = func(curr.value, accum)
            curr = curr.next
        return accum

    # functional programming in a non-functional language
    def altstr(self):
        sep = ', '
        result = self._traverse(lambda value, accumulator : accumulator + str(value) + sep , '')
        result = result[:len(result) - len(sep)]
        return '[' + result + ']'
    
    # ---- back to normal ----

    def append(self, value):
        t = LinkedNode(value)

        curr = self
        while curr.next is not None:
            curr = curr.next
        curr.next = t
        return
    
    # check if this linked list is a palindrome.
    def is_palindrome(self):
        l = []
        curr = self
        while curr is not None: # construct a 'stack' by reference
            l.append(curr.value)
            curr = curr.next

        curr = self
        while curr is not None:
            reverse = l.pop()
            if reverse != curr.value:
                return False
            curr = curr.next
        return True
    
    # return half of this linked list. If the list is odd, return the floor of half of this linked list.
    def halve_list(self):
        half = []
        counter = self
        cleaner = self
        while counter is not None:
            half.append(cleaner.value)
            cleaner = cleaner.next # be careful here.
            
            counter = counter.next
            if counter is None: # odd number of els in the linked list
                half = half[:-1]
                break
            counter = counter.next
        return half, cleaner

    # check if this linked list is a palindrome, using 'runner' approach to get only half.
    def is_palindrome_runner(self):
        l, curr = self.halve_list()
        for i in range(len(l)):
            reverse = l.pop()
            if reverse != curr.value:
                return False
            curr = curr.next
        return True

    # even more methods
    def delete_interior(self, node):
        # not allowed to access head of linked list(!)
        
        if node.next is None:
            print("Oops, tried to delete non-internal node")
            return
        node.value = node.next.value # har har har
        node.next = node.next.next
        return
    
    # remove the duplicates from the linked list using a temporary buffer.
    def delete_duplicates(self):
        buf = set()
        buf.add(self.value) # add the first value by default.
        curr = self.next
        prev = self
       
        while curr is not None:
            if curr.value in buf:
                prev.next = curr.next
            
            else:
                buf.add(curr.value)
                prev = prev.next # !! only do this if we didn't delete the node.
            
            curr = curr.next


        return

if __name__ == '__main__':
    unittest.main()
