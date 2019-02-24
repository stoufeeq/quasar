
from itertools import permutations
import unittest

def largest(l): 
    lst = [] 
    for i in permutations(l, len(l)): 
        # provides all permutations of the list values, 
        # store them in list to find max 
        lst.append("".join(map(str,i)))  
    return max(lst) 
 

class TestLargestNumner(unittest.TestCase):
    
    def test_largest_number(self):
        self.assertEqual(95486054654, int(largest([54, 546, 9548, 60])))

unittest.main(exit=False)


  