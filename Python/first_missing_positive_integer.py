# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.


arr = [3, 3, -1, 1, 2, 5]
ar1 = [1, 2, 0]
arr.sort()

for i in range(len(arr)):

    if i + 1 < len(arr):
        if arr[i + 1] - arr[i] > 1 and arr[i] + 1 != 0:
            num = arr[i] + 1
            print(num)
            break
    else:
        print(arr[i] + 1)