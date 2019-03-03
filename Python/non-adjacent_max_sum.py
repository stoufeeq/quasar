# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
# Numbers can be 0 or negative.
#
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10,
# since we pick 5 and 5.
#
# Follow-up: Can you do this in O(N) time and constant space?


def max_adjacent_sum(arr):
    incl = 0
    excl = 0

    for i in arr:
        # Current max excluding i
        new_excl = max(excl, incl)

        # Current max including i
        incl = excl + i
        excl = new_excl

        # Return max of incl and excl
    return max(excl, incl)


print(max_adjacent_sum([5, 1, 1, 5]))
print(max_adjacent_sum([2, 4, 6, 2, 5]))
