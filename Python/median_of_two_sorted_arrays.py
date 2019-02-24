#Median of two sorted arrays of different Lengths

import numpy as np

arr1 = np.array([3,5,1,6,4,7])
arr2 = np.array([7,5,0,4,9,11,13,12,17,15])

print(np.median(np.concatenate([arr1, arr2])))
