# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.

import datetime


ar1 = [3, 3, -1, 1, 2, 5]
ar2 = [1, 2, 0]
ar3 = [5, 7, 9, 3, -1, 4, 2]
ar4 = [-5, -6, -2, -3, -1]


def funct(arr):
    arr.sort()
    if arr[-1] < 0:
        return 1
    for i in range(len(arr)):
        if i + 1 < len(arr):
            if arr[i] < 0 and arr[i+1] > 1:
                return 1
            if arr[i + 1] - arr[i] > 1 and arr[i] + 1 != 0:
                num = arr[i] + 1
                return num
        else:
            num = arr[i] + 1
            return num


for i in [ar1, ar2, ar3, ar4]:
    t1 = datetime.datetime.now()
    print("\n", i, " : ", funct(i))
    t2 = datetime.datetime.now()
    print("time: ", t2-t1)
