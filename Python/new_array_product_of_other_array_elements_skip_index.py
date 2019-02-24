# Given an array of integers, return a new array such that each element at index i of the new array is the product
# of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?


def multiplier(arr):
    element = 1
    for i in range(len(arr)):
        element = element * arr[i]
    return element


def array_element_product(ar):
    product = multiplier(ar)
    new_arr = []
    for i in range(len(ar)):
        new_arr.append(int(product/ar[i]))
    return new_arr


def array_element_product_without_division(arr):
    new_arr = []
    for i in range(len(arr)):
        temp_arr = arr.copy()
        temp_arr[i] = 1
        temp_arr_product = multiplier(temp_arr)
        new_arr.append(temp_arr_product)
    return new_arr


print(array_element_product([1,2,3,4,5]))


print(array_element_product_without_division([1,2,3,4,5]))
