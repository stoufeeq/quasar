#Given an array of integers and a sum, output the number of pairs  whose addition is equal to the given sum

import numpy as np

def pairs(ar, s_sum):
    output = []
    for i in range(len(ar)):
        j = i + 1
        while j <= (len(ar) - 1):
            if ar[i] + ar[j] == s_sum:
                output.append([ar[i], ar[j]])
                #to avoid reuse of these elements:
                ar[i] = s_sum + 1
                ar[j] = s_sum + 1
            j = j + 1
    return output
my_arr = np.array([2,2,3,3,2,3,0,5,5,4,6,1,7,3,10])
print(pairs(my_arr, 11))