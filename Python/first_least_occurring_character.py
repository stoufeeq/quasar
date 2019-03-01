#least occurring character in the string:

str1 = "hhddbbsffppqqaaa"

temp_dict = dict()
temp_list = list()

for i in str1:
    temp_dict[i] = 0
    
for i in str1:
    temp_dict[i] = temp_dict[i] + 1
    
value = list(sorted(temp_dict.values()))[0]

for key in temp_dict.keys():
    if temp_dict[key] <= value:
        temp_list.append(key)
        
        
for item in str1:
    if item in temp_list:
        print(item, temp_dict[item])
        break
