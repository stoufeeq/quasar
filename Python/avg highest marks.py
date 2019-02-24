"""2: given array of students and their marks in different subjects. Find maximum average of the student.
{“James”, “70”}, {“Fernando”, “90”}, {“Nick”, “60”}, {“James”, “10”}
Ans should be name = Fernando, max avg =90"""

import numpy as np
input_arr = np.array([["James", "70"], ["Fernando", "90"], ["Nick", "60"], ["James", "70"], ["Fernando", "80"], ["Nick", "65"], ["Edward", "19"]])

marks_dic = {}
max_marks = 0
for i in input_arr:
    name = i[0]
    marks = i[1]
    if name not in marks_dic:
        marks_dic.update({name: marks})
    elif name in marks_dic:
        avg_marks = int((int(marks_dic[name]) + int(marks))/2)
        marks_dic.update({name: avg_marks}) 

for name in marks_dic: 
    if int(marks_dic[name]) > max_marks:
        max_name = name
        max_marks = int(marks_dic[name])


print("name= ", max_name, ", max avg= ", marks_dic[max_name])