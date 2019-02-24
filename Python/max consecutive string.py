#max consecutive string

str1 = "hdddddddykkkkkkkkkkkkkkkyyyyyyyyydddkkkkkklkldklglskfkddfkdyyyyyyyyyyyyyyydd"

def max_consecutive_string(str1):
    cur_count = 1
    str_count = 1

    for i in range(len(str1)-1):
        if str1[i] == str1[i+1]:
            cur_count += 1
            if cur_count > str_count:
                result = str1[i]
                str_count = cur_count
        else:
            cur_count = 1
    return result, str_count


def main():
    print(max_consecutive_string(str1))

if __name__ == "__main__":
    main()

