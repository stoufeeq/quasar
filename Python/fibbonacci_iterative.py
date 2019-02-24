def fib(n):
    a, b = 0, 1
    print(0)
    for i in range(0, n-1):
        a, b = b, a + b
        print(a)
    
fib(21)