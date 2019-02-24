def reverseStr(obj):
    length = len(obj)
    newList = []
    i = 0
    while i < length:
        newList.append((obj[length-1-i]))
        i += 1
    if type(mystr) == str:
        return ''.join(newList)
    elif type(mystr) == list:
        return newList

print(reverseStr(['a','b','c','d']))



string = "poiuytrewq"
print(string[::-1])