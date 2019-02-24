import numpy as np

a1 = np.array([19, 14, 6, 11, -16, 14, -16, -9, 16, 13])
a2 = np.array([13, 9, -15, -2, -18, 16, 17, 2, -11, -7])

target = -15

a1.sort()
a2.sort()

m = len(a1) - 1
n = 0

sum_list = list()
max_diff = abs(a1[0] + a2[0] - target)


def closest_sum(m, n, diff=max_diff):

    if m >= 0 and n < len(a2):
        sum_ar = a1[m] + a2[n]
        if sum_ar == target:
            sum_list.clear()
            sum_list.append([a1[m], a2[n]])
        elif sum_ar > target and (abs(sum_ar - target) <= diff):
            sum_list.clear()
            sum_list.append([a1[m], a2[n]])
            m = m - 1
            closest_sum(m, n, diff=abs(sum_ar - target))
        elif sum_ar < target and (abs(target - sum_ar) <= diff):
            sum_list.clear()
            sum_list.append([a1[m], a2[n]])
            n = n + 1
            closest_sum(m, n, diff=abs(target - sum_ar))
        else:
            n = n + 1
            m = m - 1
            closest_sum(m, n, diff=abs(target - sum_ar))
        return sum_list


print(closest_sum(m, n))


a1 = [19, 14, 6, 11, -16, 14, -16, -9, 16, 13]
a2 = [13, 9, -15, -2, -18, 16, 17, 2, -11, -7]
a_target = -15


def closest_sum_pair(a1, a2, target):
    a1_sorted = sorted(a1)
    a2_sorted = sorted(a2)
    i = 0
    j = len(a2_sorted) - 1
    smallest_diff = abs(a1_sorted[0] + a2_sorted[0] - target)
    closest_pair = (a1_sorted[0], a2_sorted[0])
    while i < len(a1_sorted) and j >= 0:
        v1 = a1_sorted[i]
        v2 = a2_sorted[j]
        current_diff = v1 + v2 - target
        if abs(current_diff) < smallest_diff:
            smallest_diff = abs(current_diff)
            closest_pair = (v1, v2)

        if current_diff == 0:
            return closest_pair
        elif current_diff < 0:
            i += 1
        else:
            j -= 1
    return closest_pair


print(closest_sum_pair(a1, a2, a_target))
