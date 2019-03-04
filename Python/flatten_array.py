arr = [[2, 3, 4], 1, 5, [3, 6]]

flat_arr = []


for i in arr:
    if type(i) == list:
        for j in i:
            flat_arr.append(j)
    else:
        flat_arr.append(i)

print(flat_arr)

