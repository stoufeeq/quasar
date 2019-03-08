x = [2, 3, 5, 1, 4, 7, 9, 5]

sm = 13

ans = list()


for i in range(len(x)):
    if x[i] == sm:
        ans = [x[i]]
        break
    temp_sum = x[i]
    tmp = list()
    tmp.append(x[i])
    for j in range(i+1, len(x)):
        temp_sum = temp_sum + x[j]
        tmp.append(x[j])
        if temp_sum == sm:
            if len(ans) == 0:
                ans = tmp
            elif len(tmp) < len(ans):
                ans = tmp
            break
        elif temp_sum > sm:
            break
        j += 1
    i += 1

print(ans)


