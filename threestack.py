import unittest

class TestThreeStack(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.stack = ThreeStack()

    def test_pushpop(self):
        TestThreeStack.stack.push(0, 42)
        rval = TestThreeStack.stack.pop(0)
        self.assertEqual(rval, 42)
        
    def test_multipushpop(self):
        for stacknum in range(3):
            for i in range(24):
                TestThreeStack.stack.push(stacknum, i + stacknum * 100) # easier debugging
       
        print(TestThreeStack.stack.array)

        temp = list(range(24))
        temp.reverse()
        expected = temp
        
        actual = []
        for i in range(24):
            actual.append(TestThreeStack.stack.pop(0))

        self.assertEqual(actual, expected)


class ThreeStack:
    """ Class uses 0-based stack nums """

    _capacity = 3 # internal capacity for single stack.
    _magic = 3 # number of stacks

    def __init__(self):
        self.array = [0, 0, 0]
        self.increase_capacity()
    
    def push(self, stacknum, val):
        if stacknum not in range(3):
            return -1 # error
        
        else:
            if self._query_size(stacknum) >= self._query_capacity():
                self.increase_capacity()
            
            insert_index = self._next_index(stacknum) # works for 0 case too
            self.array[insert_index] = val
            self._incr_size(stacknum)

    def pop(self, stacknum):
        if stacknum not in range(3):
            return -1
        else:
            if self._query_size(stacknum) == 0:
                return None
            else:
                popindex = self._last_index(stacknum)
                self._decr_size(stacknum)
                return self.array[popindex] # don't erase values on pop


    def _query_capacity(self):
        _magic = ThreeStack._magic
        return (len(self.array) - _magic) // _magic

    def _query_size(self, stacknum):
        return self.array[stacknum]
    
    def _incr_size(self, stacknum):
        self.array[stacknum] += 1

    def _decr_size(self, stacknum):
        self.array[stacknum] -= 1

    # index of the last item, if stack is non-empty.
    def _last_index(self, stacknum):
        _capacity = ThreeStack._capacity
        _magic = ThreeStack._magic

        size = self._query_size(stacknum)
        l = size // _capacity # this all works because size = index + 1, floor + 1 is ceiling
        if (size % _capacity) == 0: # hacky 'error-handling'
            return (l - 1) * (_magic * _capacity) + (stacknum * _capacity) + (_capacity - 1) + _magic
        return l * (_magic * _capacity) + (stacknum * _capacity) + size % _capacity + _magic - 1# offset

    def _next_index(self, stacknum):
        _capacity = ThreeStack._capacity
        _magic = ThreeStack._magic

        size = self._query_size(stacknum)
        l = size // _capacity
        return l * (_magic * _capacity) + (stacknum * _capacity) + size % _capacity + _magic  

    def increase_capacity(self):
        _capacity = ThreeStack._capacity
        _magic = ThreeStack._magic
        
        zeros = [0 for i in range(_capacity * _magic)]
        self.array += zeros

if __name__ == "__main__":
    print("Hello world")

    unittest.main()

