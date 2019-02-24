def palindrome(num):
    digits = len(str(num))
    if digits % 2 == 0:
        limit = digits/2
    else:
        limit = (digits -1)/2
    for i in range(int(limit)):
        if str(num)[i] == str(num)[-i]:
            result = "Palindrome"
        else:
            result = "Not Palindrome"
    print(num, " is ", result)

palindrome(100001)



def palindrome(num):
    original = str(num)
    temp = []
    i = 0
    while i < len(original):
        temp.append(original[len(original)-1-i])
        i += 1
    reversedNum = ''.join(temp)
    if int(reversedNum) == num:
        print(num, " is a palindrome")
    else:
        print(num, "is not a palindrome")

palindrome(12344321)