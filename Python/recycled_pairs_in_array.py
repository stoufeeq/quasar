ar = ['231', '123', '91', '19', '52', '14', '25', '8341', '3418']


st = list()


def rotation(string, k):
    if k < len(string)-1 and len(string) > 0:
        s = string[1:] + string[0]
        if int(s) < int(string) and s not in st:
            st.append(s)
        k += 1
        rotation(s, k)
    return st


for i in ar:
    x = rotation(i, 0)
    if len(x) != 0:
        for j in x:
            if j in ar:
                ar.remove(j)
                print(i, j)
                st.clear()
