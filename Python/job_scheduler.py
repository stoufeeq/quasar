# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

# for repeated call of the function:
import time as t


def job_scheduler(func, n):
    i = 0
    while i < 10:
        func()
        t.sleep(n/1000)
        i += 1


def f():
    print("running function f")


job_scheduler(f, 100)


# for delayed execution

from threading import Thread
import time


def delayed_execution(f, ms):
    time.sleep(ms)
    return f()


def hello(name):
    print('Hello there', format(name))


job = Thread(target=delayed_execution, args=(lambda: hello('from thread'), 0.1))
job.start()

print('Before')
time.sleep(0.2)
print('After')