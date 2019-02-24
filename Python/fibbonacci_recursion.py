def fib(n):
    if n <= 1:
        return n
    else:
        return(fib(n-1) + fib(n-2))


def printFib(terms):
    if terms < 1:
        print("Enter positive integer")
    for i in range(terms):
        print(fib(i))
        
printFib(21)




#with test case:
import unittest

def fib(n):
    if n <= 1:
        return n
    else:
        return(fib(n-1) + fib(n-2))


def printFib(terms):
    result = list()
    if terms < 1:
        return "Enter positive integer"
    for i in range(terms):
        result.append(fib(i))
    return(result)
        
class FibWithRecursion(unittest.TestCase):
    
    def testFib(self):
        self.assertEqual([0,1,1,2,3,5,8], printFib(7))
        
unittest.main(exit=False)