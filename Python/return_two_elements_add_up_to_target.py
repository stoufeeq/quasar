# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?

ar = [10, 15, 3, 7, 4, 9, 10, 8, 12, 2, 5]

target = 19


# double pass:

def double_pass(arr, k):
    result = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == k and i != j:
                result = (arr[i], arr[j])
    return result


print(double_pass(ar, target))


def hidden_double_pass(arr, k):
    result = 0
    for i in arr:
        if k - i in arr:
            result = (i, k - i)
    return result


print(hidden_double_pass(ar, target))


# single pass - best approach - given unique pairs if the request is to find all pairs which add up to k:


def single_pass(arr, k):
    s = set()
    result = 0
    for i in arr:
        temp = k - i
        if temp in s:
            result = (i, temp)
        s.add(i)
    return result


print(single_pass(ar, target))
