#longest subsequence of duplicate numbers in array of sorted numbers:

arr = [1, 5, 9, 11, 11, 12, 14, 16, 16, 16, 16, 16, 19, 19, 19, 19, 19, 19, 20, 21, 21, 23, 43]
my_dict = {}

for i in arr:
    if not my_dict.get(i):
        my_dict.update({i: 1})
    else:
        my_dict[i] += 1

max_key = max(my_dict, key=lambda k: my_dict[k])

new_arr = []

for i in range(my_dict[max_key]):
    new_arr.append(max_key)

print(new_arr)

